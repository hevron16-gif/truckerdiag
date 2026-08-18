(() => {
  "use strict";

  function resolveApiBase() {
    const params = new URLSearchParams(location.search);
    const fromQuery = (params.get("api") || "").trim();
    if (fromQuery) {
      const cleaned = fromQuery.replace(/\/$/, "");
      try {
        localStorage.setItem("truckerdiag_api", cleaned);
      } catch {
        /* ignore quota / private mode */
      }
      return cleaned;
    }
    let stored = "";
    try {
      stored = (localStorage.getItem("truckerdiag_api") || "").trim();
    } catch {
      stored = "";
    }
    if (stored) return stored.replace(/\/$/, "");
    const fromConfig =
      typeof window.TRUCKERDIAG_API === "string" ? window.TRUCKERDIAG_API.trim() : "";
    if (fromConfig) return fromConfig.replace(/\/$/, "");
    const host = location.hostname;
    if (host === "localhost" || host === "127.0.0.1") {
      return "http://localhost:8000";
    }
    return location.origin;
  }

  const API_BASE = resolveApiBase();

  const VEHICLES = {
    "Howo A7": ["WD615", "WP10"],
    "Howo T7H": ["MC11", "MC13", "WP13"],
    "Howo T5G": ["MC07", "WP7", "WP10"],
    "Sitrak C7H": ["MC11", "MC13", "WP13"],
    "Sitrak C9H": ["MC13", "MC11", "WP13"],
    "Shacman X3000": ["WP12", "WP13", "ISM11"],
    "Shacman F3000": ["WP10", "WP12", "WD615"],
    "Shacman H3000": ["WP10", "WP12"],
    "Shacman 6000 (X6000)": ["WP13", "WP12", "MC13"],
    "FAW J6": ["WP10", "WP12", "CA6DM2"],
    "FAW JH6": ["WP13", "WP12", "CA6DM3"],
    "Dongfeng": ["WP10", "WP12", "WP13", "ISLe"],
    "Foton Auman": ["WP10", "WP12", "ISG"],
    "Yutong ZK6122": ["YC6L", "WP10", "ISDe"],
  };

  const VEHICLE_ALIASES = {
    "f3000": "Shacman F3000",
    "shacman f3000": "Shacman F3000",
    "h3000": "Shacman H3000",
    "shacman h3000": "Shacman H3000",
    "x3000": "Shacman X3000",
    "shacman 6000": "Shacman 6000 (X6000)",
    "shacman x6000": "Shacman 6000 (X6000)",
    "x6000": "Shacman 6000 (X6000)",
  };

  function enginesFor(model) {
    const raw = String(model || "").trim();
    if (VEHICLES[raw] && VEHICLES[raw].length) return VEHICLES[raw];
    const lower = raw.toLowerCase();
    if (VEHICLE_ALIASES[lower] && VEHICLES[VEHICLE_ALIASES[lower]]) {
      return VEHICLES[VEHICLE_ALIASES[lower]];
    }
    const hit = Object.keys(VEHICLES).find((k) => k.toLowerCase() === lower);
    return hit ? VEHICLES[hit] : null;
  }

  const SEVERITY_LABELS = {
    can_drive: "Можно ехать",
    limited: "Ограниченно",
    tow: "Эвакуатор",
  };

  const $ = (id) => document.getElementById(id);

  const state = {
    step: 1,
    photoFile: null,
    photoUrl: null,
  };

  // ——— DOM ———
  const els = {
    model: $("vehicle-model"),
    engine: $("engine"),
    year: $("year"),
    errorCode: $("error-code"),
    vehicleSummary: $("vehicle-summary"),
    photoInput: $("photo-input"),
    uploadZone: $("upload-zone"),
    photoPreview: $("photo-preview"),
    photoPreviewWrap: $("photo-preview-wrap"),
    btnDiagnosePhoto: $("btn-diagnose-photo"),
    resultContent: $("result-content"),
    loading: $("loading"),
    loadingText: $("loading-text"),
    toast: $("toast"),
    apiStatus: $("api-status"),
    apiUrlLabel: $("api-url-label"),
  };

  // ——— Utils ———
  function showToast(message, isError = false) {
    els.toast.textContent = message;
    els.toast.classList.toggle("error", isError);
    els.toast.hidden = false;
    clearTimeout(showToast._t);
    showToast._t = setTimeout(() => {
      els.toast.hidden = true;
    }, 3500);
  }

  function setLoading(on, text = "Диагностика…") {
    els.loading.hidden = !on;
    els.loadingText.textContent = text;
  }

  function goTo(step) {
    state.step = step;
    for (let i = 1; i <= 3; i++) {
      const screen = $(`screen-${i}`);
      if (screen) screen.hidden = i !== step;
      const stepBtn = document.querySelector(`.step[data-step="${i}"]`);
      if (stepBtn) {
        stepBtn.classList.toggle("active", i === step);
        stepBtn.classList.toggle("done", i < step);
      }
    }
    if (step === 2) {
      const y = els.year.value || "—";
      els.vehicleSummary.textContent = `${els.model.value} · ${els.engine.value} · ${y}`;
    }
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function fillModels() {
    const current = els.model.value;
    els.model.innerHTML = Object.entries(VEHICLES)
      .map(([m, engines]) =>
        `<option value="${escapeHtml(m)}" data-engines="${escapeHtml(engines.join(","))}">${escapeHtml(m)}</option>`
      )
      .join("");
    if (current && enginesFor(current)) els.model.value = current;
    if (!els.model.value) {
      const first = Object.keys(VEHICLES)[0];
      if (first) els.model.value = first;
    }
  }

  function fillEngines() {
    const opt = els.model.options[els.model.selectedIndex];
    const fromAttr = opt && opt.dataset.engines
      ? opt.dataset.engines.split(",").map((s) => s.trim()).filter(Boolean)
      : [];
    const engines = fromAttr.length ? fromAttr : (enginesFor(els.model.value) || []);
    if (!engines.length) {
      els.engine.innerHTML = "";
      return;
    }
    els.engine.innerHTML = engines
      .map((e, i) => `<option value="${escapeHtml(e)}" ${i === 0 ? "selected" : ""}>${escapeHtml(e)}</option>`)
      .join("");
  }

  function switchTab(name) {
    document.querySelectorAll(".tab").forEach((t) => {
      const on = t.dataset.tab === name;
      t.classList.toggle("active", on);
      t.setAttribute("aria-selected", on ? "true" : "false");
    });
    $("panel-manual").hidden = name !== "manual";
    $("panel-photo").hidden = name !== "photo";
  }

  function clearPhoto() {
    if (state.photoUrl) URL.revokeObjectURL(state.photoUrl);
    state.photoFile = null;
    state.photoUrl = null;
    els.photoInput.value = "";
    els.photoPreview.removeAttribute("src");
    els.photoPreviewWrap.hidden = true;
    els.btnDiagnosePhoto.disabled = true;
  }

  function setPhoto(file) {
    if (!file || !file.type.startsWith("image/")) {
      showToast("Нужен файл изображения", true);
      return;
    }
    if (file.size > 5 * 1024 * 1024) {
      showToast("Файл больше 5 МБ", true);
      return;
    }
    if (state.photoUrl) URL.revokeObjectURL(state.photoUrl);
    state.photoFile = file;
    state.photoUrl = URL.createObjectURL(file);
    els.photoPreview.src = state.photoUrl;
    els.photoPreviewWrap.hidden = false;
    els.btnDiagnosePhoto.disabled = false;
  }

  // ——— API ———
  async function checkHealth() {
    els.apiUrlLabel.textContent = API_BASE.replace(/^https?:\/\//, "");
    try {
      const r = await fetch(`${API_BASE}/health`, { method: "GET" });
      const ok = r.ok;
      els.apiStatus.classList.toggle("online", ok);
      els.apiStatus.classList.toggle("offline", !ok);
      els.apiStatus.title = ok ? "API онлайн" : "API недоступен";
      return ok;
    } catch {
      els.apiStatus.classList.remove("online");
      els.apiStatus.classList.add("offline");
      els.apiStatus.title = "API недоступен";
      return false;
    }
  }

  async function diagnoseManual() {
    const error_code = (els.errorCode.value || "").trim().toUpperCase();
    if (!error_code) {
      showToast("Введите код ошибки", true);
      els.errorCode.focus();
      return;
    }

    const year = parseInt(els.year.value, 10);
    if (!year || year < 1990 || year > 2030) {
      showToast("Укажите корректный год", true);
      return;
    }

    setLoading(true, "Запрос к ИИ-диагносту…");
    try {
      const res = await fetch(`${API_BASE}/diagnose`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          vehicle_model: els.model.value,
          engine: els.engine.value,
          year,
          error_code,
        }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || `Ошибка сервера ${res.status}`);
      }

      const data = await res.json();
      renderResult({
        codes: [error_code],
        diagnoses: [normalizeDiagnosis(data, error_code)],
        ocrText: null,
      });
      goTo(3);
    } catch (e) {
      showToast(humanError(e), true);
    } finally {
      setLoading(false);
    }
  }

  async function diagnosePhoto() {
    if (!state.photoFile) {
      showToast("Сначала выберите фото", true);
      return;
    }

    const year = parseInt(els.year.value, 10) || 2019;
    setLoading(true, "OCR + диагностика…");
    try {
      const form = new FormData();
      form.append("photo", state.photoFile, state.photoFile.name || "scanner.jpg");
      form.append("vehicle_model", els.model.value);
      form.append("engine", els.engine.value);
      form.append("year", String(year));

      const res = await fetch(`${API_BASE}/diagnose-photo`, {
        method: "POST",
        body: form,
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(
          typeof err.detail === "string" ? err.detail : err.detail?.message || `Ошибка ${res.status}`
        );
      }

      const data = await res.json();
      const parsed = parsePhotoResponse(data);
      if (!parsed.diagnoses.length) {
        showToast(data.error || "Коды ошибок не распознаны", true);
        return;
      }
      renderResult(parsed);
      goTo(3);
    } catch (e) {
      showToast(humanError(e), true);
    } finally {
      setLoading(false);
    }
  }

  function humanError(e) {
    const msg = String(e.message || e);
    if (msg.includes("Failed to fetch") || msg.includes("NetworkError") || msg.includes("Load failed")) {
      return "Нет связи с API. Запустите backend на :8000";
    }
    return msg;
  }

  function normalizeDiagnosis(d, code) {
    if (!d || typeof d !== "object") {
      return {
        error_description: "Нет данных",
        top_causes: [],
        check_steps: [],
        severity: "limited",
        estimated_time_min: null,
        practical_advice: "",
        images: [],
      };
    }
    return {
      error_description: d.error_description || "—",
      top_causes: Array.isArray(d.top_causes) ? d.top_causes : [],
      check_steps: Array.isArray(d.check_steps) ? d.check_steps : [],
      severity: d.severity || "limited",
      estimated_time_min: d.estimated_time_min ?? null,
      practical_advice: d.practical_advice || "",
      images: normalizeImages(d.images),
    };
  }

  function normalizeImages(raw) {
    if (!Array.isArray(raw)) return [];
    return raw
      .map((img) => {
        if (!img || typeof img !== "object") return null;
        const file = String(img.file || img.src || "").replace(/^.*[\\/]/, "").trim();
        if (!file || file.includes("..")) return null;
        return {
          file,
          src: "images/" + file,
          caption: String(img.caption || "").trim(),
        };
      })
      .filter(Boolean);
  }

  /** Поддержка формата из ТЗ и реального ответа FastAPI */
  function parsePhotoResponse(data) {
    // ТЗ: { ocr_text, detected_codes, diagnosis }
    if (data.diagnosis || data.detected_codes) {
      const codes = data.detected_codes || [];
      const diagnoses = data.diagnosis
        ? [normalizeDiagnosis(data.diagnosis, codes[0])]
        : (data.diagnoses || []).map((d, i) => normalizeDiagnosis(d, codes[i]));
      return {
        codes,
        diagnoses,
        ocrText: data.ocr_text || null,
      };
    }

    // FastAPI: { ocr_result, diagnoses }
    if (data.diagnoses || data.ocr_result) {
      const ocr = data.ocr_result || {};
      return {
        codes: ocr.error_codes || data.detected_codes || [],
        diagnoses: (data.diagnoses || []).map((d, i) =>
          normalizeDiagnosis(d, (ocr.error_codes || data.detected_codes || [])[i])
        ),
        ocrText: ocr.notes || null,
        ocrVehicle: ocr.vehicle_model || null,
      };
    }

    if (data.error) {
      return { codes: [], diagnoses: [], ocrText: JSON.stringify(data.ocr_raw || data) };
    }

    return { codes: [], diagnoses: [normalizeDiagnosis(data)], ocrText: null };
  }

  // ——— Render ———
  function severityBadge(severity) {
    const key = SEVERITY_LABELS[severity] ? severity : "limited";
    const label = SEVERITY_LABELS[key] || severity;
    return `<span class="badge badge-${key}">${escapeHtml(label)}</span>`;
  }

  function renderCause(c) {
    const cause = c.cause || c.name || "—";
    const pct = Number(c.probability ?? c.percent ?? 0);
    const oem = c.oem_part || c.part || c.oem || "";
    const comment = c.comment || "";
    const width = Math.max(0, Math.min(100, pct));
    return `
      <li class="cause-item">
        <div class="cause-top">
          <span class="cause-name">${escapeHtml(cause)}</span>
          <span class="cause-pct">${pct ? pct + "%" : "—"}</span>
        </div>
        <div class="bar"><div class="bar-fill" style="width:${width}%"></div></div>
        ${
          comment
            ? `<p class="cause-comment">${escapeHtml(String(comment))}</p>`
            : ""
        }
        ${
          oem
            ? `<div class="oem">OEM: <code>${escapeHtml(String(oem))}</code></div>`
            : ""
        }
      </li>`;
  }

  function renderDiagnosisCard(diag, code, index, total) {
    const title =
      total > 1
        ? `<h2 class="result-code">${escapeHtml(code || "Код " + (index + 1))}</h2>`
        : code
          ? `<h2 class="result-code">${escapeHtml(code)}</h2>`
          : `<h2 class="result-code">Результат</h2>`;

    const time =
      diag.estimated_time_min != null
        ? `<span class="meta-chip">⏱ ~${escapeHtml(String(diag.estimated_time_min))} мин</span>`
        : "";

    const causes =
      diag.top_causes.length > 0
        ? `<ul class="cause-list">${diag.top_causes.map(renderCause).join("")}</ul>`
        : `<p class="oem">Причины не указаны</p>`;

    const steps =
      diag.check_steps.length > 0
        ? `<ol class="steps-list">${diag.check_steps
            .map((s) => `<li>${escapeHtml(String(s))}</li>`)
            .join("")}</ol>`
        : `<p class="oem">Шаги не указаны</p>`;

    return `
      <article class="multi-diag">
        <div class="result-header">
          ${title}
          ${severityBadge(diag.severity)}
        </div>
        <div class="meta-row">
          <span class="meta-chip">${escapeHtml(els.model.value)}</span>
          <span class="meta-chip">${escapeHtml(els.engine.value)}</span>
          <span class="meta-chip">${escapeHtml(els.year.value)}</span>
          ${time}
        </div>
        <div class="card">
          <h3 class="card-title">Описание</h3>
          <p>${escapeHtml(diag.error_description)}</p>
        </div>
        ${renderImageGallery(diag.images)}
        <div class="card">
          <h3 class="card-title">Вероятные причины</h3>
          ${causes}
        </div>
        <div class="card">
          <h3 class="card-title">Пошаговая проверка</h3>
          ${steps}
        </div>
        ${
          diag.practical_advice
            ? `<div class="card">
          <h3 class="card-title">Можно ли ехать</h3>
          <p>${escapeHtml(diag.practical_advice)}</p>
        </div>`
            : ""
        }
      </article>`;
  }

  function renderImageGallery(images) {
    if (!images || !images.length) return "";
    const payload = encodeURIComponent(JSON.stringify(images));
    const items = images
      .map((img, i) => {
        const cap = img.caption || "Справочное фото";
        return `<button type="button" class="ref-thumb" data-ref-index="${i}" aria-label="${escapeHtml(cap)}">
          <img src="${escapeHtml(img.src)}" alt="${escapeHtml(cap)}" loading="lazy" />
          <span class="ref-thumb-cap">${escapeHtml(cap)}</span>
        </button>`;
      })
      .join("");
    return `<div class="card">
        <h3 class="card-title">Как выглядит узел</h3>
        <div class="ref-gallery" data-ref-images="${payload}">${items}</div>
      </div>`;
  }

  const lightbox = {
    items: [],
    index: 0,
    el: null,
    img: null,
    cap: null,
    counter: null,
  };

  function ensureLightbox() {
    if (lightbox.el) return lightbox.el;
    const root = document.createElement("div");
    root.id = "lightbox";
    root.className = "lightbox";
    root.hidden = true;
    root.innerHTML = `
      <button type="button" class="lightbox-close" aria-label="Закрыть">×</button>
      <button type="button" class="lightbox-nav lightbox-prev" aria-label="Предыдущее">‹</button>
      <figure class="lightbox-figure">
        <img alt="" />
        <figcaption>
          <span class="lightbox-cap"></span>
          <span class="lightbox-counter"></span>
        </figcaption>
      </figure>
      <button type="button" class="lightbox-nav lightbox-next" aria-label="Следующее">›</button>`;
    document.body.appendChild(root);
    lightbox.el = root;
    lightbox.img = root.querySelector("img");
    lightbox.cap = root.querySelector(".lightbox-cap");
    lightbox.counter = root.querySelector(".lightbox-counter");

    root.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
    root.querySelector(".lightbox-prev").addEventListener("click", (e) => {
      e.stopPropagation();
      stepLightbox(-1);
    });
    root.querySelector(".lightbox-next").addEventListener("click", (e) => {
      e.stopPropagation();
      stepLightbox(1);
    });
    root.addEventListener("click", (e) => {
      if (e.target === root) closeLightbox();
    });
    document.addEventListener("keydown", (e) => {
      if (root.hidden) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft") stepLightbox(-1);
      if (e.key === "ArrowRight") stepLightbox(1);
    });
    return root;
  }

  function openLightbox(items, index) {
    if (!items || !items.length) return;
    ensureLightbox();
    lightbox.items = items;
    lightbox.index = index;
    paintLightbox();
    lightbox.el.hidden = false;
    document.body.classList.add("lightbox-open");
  }

  function closeLightbox() {
    if (!lightbox.el) return;
    lightbox.el.hidden = true;
    document.body.classList.remove("lightbox-open");
  }

  function stepLightbox(delta) {
    const n = lightbox.items.length;
    if (!n) return;
    lightbox.index = (lightbox.index + delta + n) % n;
    paintLightbox();
  }

  function paintLightbox() {
    const item = lightbox.items[lightbox.index];
    if (!item) return;
    lightbox.img.src = item.src;
    lightbox.img.alt = item.caption || "";
    lightbox.cap.textContent = item.caption || "";
    lightbox.counter.textContent =
      lightbox.items.length > 1 ? `${lightbox.index + 1} / ${lightbox.items.length}` : "";
    const many = lightbox.items.length > 1;
    lightbox.el.querySelector(".lightbox-prev").hidden = !many;
    lightbox.el.querySelector(".lightbox-next").hidden = !many;
  }

  function renderResult({ codes, diagnoses, ocrText, ocrVehicle }) {
    let html = "";

    if (ocrText || (codes && codes.length) || ocrVehicle) {
      html += `<div class="card ocr-block">
        <h3 class="card-title">Распознано со сканера</h3>
        ${ocrVehicle ? `<p>Модель на экране: <strong>${escapeHtml(ocrVehicle)}</strong></p>` : ""}
        ${
          codes && codes.length
            ? `<div class="ocr-codes">${codes
                .map((c) => `<span class="ocr-code-chip">${escapeHtml(String(c))}</span>`)
                .join("")}</div>`
            : ""
        }
        ${ocrText ? `<p class="oem" style="margin-top:8px">${escapeHtml(String(ocrText))}</p>` : ""}
      </div>`;
    }

    diagnoses.forEach((d, i) => {
      const code = codes[i] || codes[0] || (els.errorCode.value || "").toUpperCase();
      html += renderDiagnosisCard(d, code, i, diagnoses.length);
    });

    els.resultContent.innerHTML = html || `<div class="card"><p>Нет данных</p></div>`;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // ——— Events ———
  function bind() {
    fillModels();
    fillEngines();
    els.model.addEventListener("change", fillEngines);

    if (els.apiUrlLabel) {
      els.apiUrlLabel.title = "Нажмите, чтобы сменить адрес API";
      els.apiUrlLabel.style.cursor = "pointer";
      els.apiUrlLabel.addEventListener("click", () => {
        const next = window.prompt("Адрес API (пусто — сбросить)", API_BASE);
        if (next == null) return;
        const cleaned = next.trim().replace(/\/$/, "");
        try {
          if (cleaned) localStorage.setItem("truckerdiag_api", cleaned);
          else localStorage.removeItem("truckerdiag_api");
        } catch {
          showToast("Не удалось сохранить адрес API", true);
          return;
        }
        location.reload();
      });
    }

    $("btn-to-code").addEventListener("click", () => goTo(2));
    $("btn-back-1").addEventListener("click", () => goTo(1));
    $("btn-back-2").addEventListener("click", () => goTo(2));
    $("btn-new").addEventListener("click", () => {
      els.errorCode.value = "";
      clearPhoto();
      goTo(1);
    });

    els.resultContent.addEventListener("click", (e) => {
      const thumb = e.target.closest(".ref-thumb");
      if (!thumb) return;
      const gallery = thumb.closest(".ref-gallery");
      if (!gallery || !gallery.dataset.refImages) return;
      try {
        const items = JSON.parse(decodeURIComponent(gallery.dataset.refImages));
        const idx = Number(thumb.dataset.refIndex) || 0;
        openLightbox(items, idx);
      } catch {
        /* ignore broken gallery payload */
      }
    });

    $("btn-diagnose").addEventListener("click", diagnoseManual);
    $("btn-diagnose-photo").addEventListener("click", diagnosePhoto);
    $("btn-clear-photo").addEventListener("click", clearPhoto);

    els.errorCode.addEventListener("keydown", (e) => {
      if (e.key === "Enter") diagnoseManual();
    });

    document.querySelectorAll(".tab").forEach((tab) => {
      tab.addEventListener("click", () => switchTab(tab.dataset.tab));
    });

    els.uploadZone.addEventListener("click", () => els.photoInput.click());
    els.photoInput.addEventListener("change", () => {
      const f = els.photoInput.files && els.photoInput.files[0];
      if (f) setPhoto(f);
    });

    ["dragenter", "dragover"].forEach((ev) => {
      els.uploadZone.addEventListener(ev, (e) => {
        e.preventDefault();
        els.uploadZone.classList.add("dragover");
      });
    });
    ["dragleave", "drop"].forEach((ev) => {
      els.uploadZone.addEventListener(ev, (e) => {
        e.preventDefault();
        els.uploadZone.classList.remove("dragover");
      });
    });
    els.uploadZone.addEventListener("drop", (e) => {
      const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
      if (f) setPhoto(f);
    });
  }

  function registerSW() {
    if (!("serviceWorker" in navigator)) return;
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("./sw.js").catch(() => {});
    });
  }

  async function maybePreview() {
    const code = new URLSearchParams(location.search).get("preview");
    if (!code) return;
    try {
      const r = await fetch(`${API_BASE}/parts-images?code=${encodeURIComponent(code)}`);
      if (!r.ok) throw new Error("Не удалось загрузить фото");
      const data = await r.json();
      els.errorCode.value = code.toUpperCase();
      renderResult({
        codes: [],
        diagnoses: [
          normalizeDiagnosis(
            {
              error_description: "Превью справочных фото. Полный текст появится после диагностики.",
              top_causes: [],
              check_steps: [],
              severity: "limited",
              estimated_time_min: null,
              images: data.images || [],
            },
            code
          ),
        ],
        ocrText: null,
      });
      goTo(3);
    } catch (e) {
      showToast(humanError(e), true);
    }
  }

  // ——— Init ———
  bind();
  goTo(1);
  checkHealth();
  maybePreview();
  setInterval(checkHealth, 30000);
  registerSW();
})();
