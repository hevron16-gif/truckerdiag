(() => {
  "use strict";

  const API_BASE = localStorage.getItem("truckerdiag_api") || "http://localhost:8000";

  const VEHICLES = {
    "Howo A7": ["WD615", "WP10", "WP12"],
    "Howo T7H": ["MC11", "MC13", "WP13"],
    "Shacman X3000": ["WP12", "WP13", "ISM11"],
    "Yutong ZK6122": ["YC6L", "WP10", "ISDe"],
  };

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

  function fillEngines() {
    const engines = VEHICLES[els.model.value] || ["—"];
    els.engine.innerHTML = engines
      .map((e, i) => `<option value="${e}" ${i === 0 ? "selected" : ""}>${e}</option>`)
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
        diagnoses: [normalizeDiagnosis(data)],
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

  function normalizeDiagnosis(d) {
    if (!d || typeof d !== "object") {
      return {
        error_description: "Нет данных",
        top_causes: [],
        check_steps: [],
        severity: "limited",
        estimated_time_min: null,
      };
    }
    return {
      error_description: d.error_description || "—",
      top_causes: Array.isArray(d.top_causes) ? d.top_causes : [],
      check_steps: Array.isArray(d.check_steps) ? d.check_steps : [],
      severity: d.severity || "limited",
      estimated_time_min: d.estimated_time_min ?? null,
    };
  }

  /** Поддержка формата из ТЗ и реального ответа FastAPI */
  function parsePhotoResponse(data) {
    // ТЗ: { ocr_text, detected_codes, diagnosis }
    if (data.diagnosis || data.detected_codes) {
      const codes = data.detected_codes || [];
      const diagnoses = data.diagnosis
        ? [normalizeDiagnosis(data.diagnosis)]
        : (data.diagnoses || []).map(normalizeDiagnosis);
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
        diagnoses: (data.diagnoses || []).map(normalizeDiagnosis),
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
    const width = Math.max(0, Math.min(100, pct));
    return `
      <li class="cause-item">
        <div class="cause-top">
          <span class="cause-name">${escapeHtml(cause)}</span>
          <span class="cause-pct">${pct ? pct + "%" : "—"}</span>
        </div>
        <div class="bar"><div class="bar-fill" style="width:${width}%"></div></div>
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
        <div class="card">
          <h3 class="card-title">Вероятные причины</h3>
          ${causes}
        </div>
        <div class="card">
          <h3 class="card-title">Пошаговая проверка</h3>
          ${steps}
        </div>
      </article>`;
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
    fillEngines();
    els.model.addEventListener("change", fillEngines);

    $("btn-to-code").addEventListener("click", () => goTo(2));
    $("btn-back-1").addEventListener("click", () => goTo(1));
    $("btn-back-2").addEventListener("click", () => goTo(2));
    $("btn-new").addEventListener("click", () => {
      els.errorCode.value = "";
      clearPhoto();
      goTo(1);
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

  // ——— Init ———
  bind();
  goTo(1);
  checkHealth();
  setInterval(checkHealth, 30000);
  registerSW();
})();
