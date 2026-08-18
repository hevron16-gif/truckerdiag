(() => {
  "use strict";

  function resolveApiBase() {
    const params = new URLSearchParams(location.search);
    const fromQuery = (params.get("api") || "").trim();
    if (fromQuery) return fromQuery.replace(/\/$/, "");
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
    if (host === "localhost" || host === "127.0.0.1") return "http://localhost:8000";
    return location.origin;
  }

  const API_BASE = resolveApiBase();

  const form = document.getElementById("comment-form");
  const nameEl = document.getElementById("comment-name");
  const textEl = document.getElementById("comment-text");
  const submitEl = document.getElementById("comment-submit");
  const statusEl = document.getElementById("comment-status");
  const listEl = document.getElementById("comments-list");

  function setStatus(message, isError) {
    statusEl.hidden = !message;
    statusEl.textContent = message || "";
    statusEl.classList.toggle("comment-status-error", Boolean(isError));
  }

  function formatDate(iso) {
    if (!iso) return "";
    const d = new Date(iso);
    if (Number.isNaN(d.getTime())) return iso;
    return d.toLocaleString("ru-RU", { dateStyle: "medium", timeStyle: "short" });
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  async function loadComments() {
    try {
      const res = await fetch(`${API_BASE}/api/comments`);
      if (!res.ok) throw new Error("Не удалось загрузить отзывы");
      const data = await res.json();
      const items = data.comments || [];
      if (!items.length) {
        listEl.innerHTML = `<p class="screen-hint">Пока нет одобренных отзывов.</p>`;
        return;
      }
      listEl.innerHTML = items
        .map(
          (c) => `
        <article class="comment-card">
          <header class="comment-meta">
            <strong>${escapeHtml(c.name)}</strong>
            <time>${escapeHtml(formatDate(c.created_at))}</time>
          </header>
          <p class="comment-body">${escapeHtml(c.text)}</p>
        </article>`
        )
        .join("");
    } catch {
      listEl.innerHTML = `<p class="screen-hint">Список отзывов сейчас недоступен.</p>`;
    }
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = (nameEl.value || "").trim();
    const text = (textEl.value || "").trim();
    if (!name || !text) {
      setStatus("Заполните имя и текст", true);
      return;
    }
    submitEl.disabled = true;
    setStatus("Отправка…", false);
    try {
      const res = await fetch(`${API_BASE}/api/comments`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, text }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        throw new Error(data.detail || "Не удалось отправить");
      }
      form.reset();
      setStatus(data.message || "Комментарий отправлен на модерацию", false);
    } catch (err) {
      setStatus(err.message || "Ошибка отправки", true);
    } finally {
      submitEl.disabled = false;
    }
  });

  loadComments();
})();
