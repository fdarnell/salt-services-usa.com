/* Weblove signature cursor — dot + trailing ring + click ripple (Template 05).
   Desktop pointers only; skipped entirely under prefers-reduced-motion, in
   which case the .wl-cursor class is never added and the native cursor stays. */
(function () {
  if (matchMedia('(pointer:coarse)').matches) return;
  if (!matchMedia('(prefers-reduced-motion: no-preference)').matches) return;
  document.body.classList.add('wl-cursor');
  var dot = document.createElement('div'); dot.id = 'wlDot';
  var ring = document.createElement('div'); ring.id = 'wlRing';
  document.body.append(dot, ring);
  var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
  addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY;
    dot.style.left = mx + 'px'; dot.style.top = my + 'px';
  });
  (function f() {
    rx += (mx - rx) * .16; ry += (my - ry) * .16;
    ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
    requestAnimationFrame(f);
  })();
  addEventListener('mousedown', function (e) {
    var r = document.createElement('div'); r.className = 'wlRipple';
    r.style.left = e.clientX + 'px'; r.style.top = e.clientY + 'px';
    document.body.appendChild(r);
    setTimeout(function () { r.remove(); }, 600);
  });
  document.querySelectorAll('a,button,summary').forEach(function (el) {
    el.addEventListener('mouseenter', function () { ring.style.width = '60px'; ring.style.height = '60px'; });
    el.addEventListener('mouseleave', function () { ring.style.width = '36px'; ring.style.height = '36px'; });
  });
})();
