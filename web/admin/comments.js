(() => {
  "use strict";

  const STORAGE_KEY = "truckerdiag_admin_password";

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
  const loginForm = document.getElementById("login-form");
  const passwordEl = document.getElementById("admin-password");
  const loginStatus = document.getElementById("login-status");
  const panel = document.getElementById("admin-panel");
  const listEl = document.getElementById("admin-list");
  const adminStatus = document.getElementById("admin-status");

  function getPassword() {
    try {
      return sessionStorage.getItem(STORAGE_KEY) || "";
    } catch {
      return "";
    }
  }

  function setPassword(value) {
    try {
      if (value) sessionStorage.setItem(STORAGE_KEY, value);
      else sessionStorage.removeItem(STORAGE_KEY);
    } catch {
      /* ignore */
    }
  }

  function setMsg(el, message, isError) {
    el.hidden = !message;
    el.textContent = message || "";
    el.classList.toggle("comment-status-error", Boolean(isError));
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatDate(iso) {
    if (!iso) return "";
    const d = new Date(iso);
    if (Number.isNaN(d.getTime())) return iso;
    return d.toLocaleString("ru-RU", { dateStyle: "medium", timeStyle: "short" });
  }

  function headers() {
    return { "X-Admin-Password": getPassword() };
  }

  async function api(path, options = {}) {
    const res = await fetch(`${API_BASE}${path}`, {
      ...options,
      headers: { ...(options.headers || {}), ...headers() },
    });
    const data = await res.json().catch(() => ({}));
    if (res.status === 401) {
      throw Object.assign(new Error(data.detail || "Неверный пароль"), { auth: true });
    }
    if (!res.ok) throw new Error(data.detail || "Ошибка запроса");
    return data;
  }

  function showLogin() {
    loginForm.hidden = false;
    panel.hidden = true;
  }

  function showPanel() {
    loginForm.hidden = true;
    panel.hidden = false;
  }

  function renderList(items) {
    if (!items.length) {
      listEl.innerHTML = `<p class="screen-hint">Комментариев пока нет.</p>`;
      return;
    }
    listEl.innerHTML = items
      .map((c) => {
        const approved = Boolean(c.is_approved);
        const badge = approved
          ? `<span class="badge badge-can_drive">одобрен</span>`
          : `<span class="badge badge-limited">скрыт</span>`;
        const approveBtn = approved
          ? ""
          : `<button type="button" class="btn btn-primary btn-sm" data-approve="${c.id}">Одобрить</button>`;
        return `
          <article class="comment-card">
            <header class="comment-meta">
              <strong>${escapeHtml(c.name)}</strong>
              ${badge}
            </header>
            <p class="screen-hint">${escapeHtml(formatDate(c.created_at))} · IP ${escapeHtml(c.ip || "—")}</p>
            <p class="comment-body">${escapeHtml(c.text)}</p>
            <div class="admin-actions">
              ${approveBtn}
              <button type="button" class="btn btn-danger btn-sm" data-delete="${c.id}">Удалить</button>
            </div>
          </article>`;
      })
      .join("");
  }

  async function loadList() {
    const data = await api("/api/admin/comments");
    renderList(data.comments || []);
  }

  async function enter(password) {
    setPassword(password);
    await loadList();
    showPanel();
    setMsg(loginStatus, "", false);
    setMsg(adminStatus, "", false);
  }

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const password = (passwordEl.value || "").trim();
    if (!password) return;
    try {
      await enter(password);
    } catch (err) {
      setPassword("");
      showLogin();
      setMsg(loginStatus, err.message || "Неверный пароль", true);
    }
  });

  listEl.addEventListener("click", async (e) => {
    const approveBtn = e.target.closest("[data-approve]");
    const deleteBtn = e.target.closest("[data-delete]");
    try {
      if (approveBtn) {
        await api(`/api/admin/comments/${approveBtn.dataset.approve}/approve`, { method: "POST" });
        await loadList();
        setMsg(adminStatus, "Комментарий одобрен", false);
      }
      if (deleteBtn) {
        if (!window.confirm("Удалить комментарий?")) return;
        await api(`/api/admin/comments/${deleteBtn.dataset.delete}`, { method: "DELETE" });
        await loadList();
        setMsg(adminStatus, "Комментарий удалён", false);
      }
    } catch (err) {
      if (err.auth) {
        setPassword("");
        showLogin();
        setMsg(loginStatus, err.message, true);
        return;
      }
      setMsg(adminStatus, err.message || "Ошибка", true);
    }
  });

  document.getElementById("admin-logout").addEventListener("click", () => {
    setPassword("");
    passwordEl.value = "";
    showLogin();
  });

  if (getPassword()) {
    enter(getPassword()).catch(() => {
      setPassword("");
      showLogin();
    });
  }
})();
