/* TruckerDiag PWA service worker */
const CACHE = "truckerdiag-v6";
const ASSETS = [
  "./",
  "./index.html",
  "./requisites.html",
  "./config.js",
  "./app.js",
  "./app.js?v=5",
  "./style.css",
  "./manifest.json",
  "./icons/icon.svg",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);

  // API — только сеть, без кэша
  if (url.port === "8000" || url.pathname.includes("/diagnose") || url.pathname.includes("/health")) {
    return;
  }

  // HTML/JS — сеть первой, чтобы список моделей не залипал в старом кэше
  const path = url.pathname;
  const isAppShell =
    path.endsWith("/") ||
    path.endsWith("/index.html") ||
    path.endsWith("/requisites.html") ||
    path.endsWith("/app.js") ||
    path.endsWith("/config.js") ||
    path.endsWith("/sw.js");

  if (url.origin === self.location.origin) {
    if (isAppShell) {
      event.respondWith(
        fetch(req)
          .then((res) => {
            if (res && res.ok) {
              const clone = res.clone();
              caches.open(CACHE).then((c) => c.put(req, clone));
            }
            return res;
          })
          .catch(() => caches.match(req))
      );
      return;
    }

    event.respondWith(
      caches.match(req).then((cached) => {
        const fetched = fetch(req)
          .then((res) => {
            if (res && res.ok) {
              const clone = res.clone();
              caches.open(CACHE).then((c) => c.put(req, clone));
            }
            return res;
          })
          .catch(() => cached);
        return cached || fetched;
      })
    );
  }
});
