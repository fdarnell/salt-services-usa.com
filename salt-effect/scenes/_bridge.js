/* Scene bridge: lets one effect page run inside the long story page (index.html).
   Load it first in every scene's <head>:  <script src="_bridge.js"></script>

   Opened on its own, a scene behaves like a normal page. Inside the story it:
   - hands wheel and arrow-key scrolling up to the story page, so the story keeps moving
     (a scene that needs the wheel for itself sets <html data-own-wheel>);
   - reports its height, so a tall scroll scene gets a section of the same height;
   - is scrolled by the story page (scroll scenes, <html data-scene="scroll">);
   - receives 'scene:progress' events, detail.p from 0 (scene entering at the bottom)
     to 1 (scene leaving at the top), for effects that should move with the story scroll;
   - receives 'scene:enter' / 'scene:leave' when it fills / leaves the screen.

   One-shot intros (counters, countdowns, line reveals) must start through
   SCENE.onFirstEnter(fn): it runs fn on load when the scene is opened alone, and the first
   time the visitor actually reaches it inside the story (scenes load a screen early). */
(function () {
  var root = document.documentElement;
  function post(m) { m.salt = 1; parent.postMessage(m, '*'); }
  var embedded = window.parent !== window;
  var firstEnter = [], entered = false;
  var S = window.SCENE = window.SCENE || {};
  S.embedded = embedded;

  // Reduced motion: CSS motion is cut, and animation frames run only briefly (on load and
  // each time the scene is reached) so every effect settles on a still picture.
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  S.reduce = reduce;
  if (reduce) {
    root.classList.add('reduce');
    var rm = document.createElement('style');
    rm.textContent = '*,*::before,*::after{animation-duration:0s!important;animation-delay:0s!important;animation-iteration-count:1!important;transition-duration:0s!important;transition-delay:0s!important;scroll-behavior:auto!important}';
    (document.head || root).appendChild(rm);
    // A short "fast-forward" instead of live motion: while warping, the scene's clock runs
    // 14x fast, so an intro finishes in a blink and the scene settles on its end state;
    // after that, animation frames are parked and the picture holds still.
    var SPEED = 14, warp = false, extra = 0;
    var pnow = performance.now.bind(performance), dnow = Date.now, lastReal = pnow();
    var step = function () { var r = pnow(); if (warp) extra += (r - lastReal) * (SPEED - 1); lastReal = r; };
    performance.now = function () { step(); return pnow() + extra; };
    Date.now = function () { step(); return dnow() + extra; };
    var st = window.setTimeout.bind(window);
    window.setTimeout = function (fn, ms) {
      var a = Array.prototype.slice.call(arguments);
      if (warp && typeof ms === 'number') a[1] = ms / SPEED;
      return st.apply(window, a);
    };
    var raf0 = window.requestAnimationFrame.bind(window), until = pnow() + 500, parked = [];
    window.requestAnimationFrame = function (cb) {
      if (pnow() < until) return raf0(function () { cb(performance.now()); });
      parked.push(cb);
      return 0;
    };
    // thaw(ms, fast): let frames run for ms of real time; fast = fast-forward intros
    S.thaw = function (ms, fast) {
      step();
      warp = fast !== false;
      until = pnow() + (ms || 500);
      st(function () { step(); warp = false; }, ms || 500);
      parked.splice(0).forEach(function (cb) { raf0(function () { cb(performance.now()); }); });
    };
    S.thaw(500);
  }
  // A scene with a light ground tells the story page so its header can switch to dark ink.
  // Scenes that change ground (e.g. a noon sky) can call SCENE.tone(true/false) themselves.
  // Scroll scenes: where a phone swipe should land, in this page's own scroll pixels (one per
  // panel, card or chapter). Call it on load and whenever the layout changes.
  S.setStops = function (ys) { if (embedded) post({ t: 'stops', ys: (ys || []).map(function (v) { return Math.round(v); }) }); };
  S.tone = function (light) { if (embedded) post({ t: 'tone', light: !!light }); };
  // A scene whose effect IS a site header (the navbar scene) can hide the story's header
  // while it is on screen: SCENE.chrome(false) on scene:enter. The story restores it on leave.
  S.chrome = function (show) { if (embedded) post({ t: 'chrome', show: !!show }); };
  S.onFirstEnter = function (fn) {
    if (entered) return fn();
    firstEnter.push(fn);
    if (!embedded) {
      if (document.readyState === 'complete') fire();
      else addEventListener('load', fire);
    }
  };
  function fire() {
    if (entered) return;
    entered = true;
    firstEnter.splice(0).forEach(function (fn) { try { fn(); } catch (e) { console.error(e); } });
  }
  if (!embedded) { root.classList.add('scene-solo'); return; }

  root.classList.add('scene-embedded');
  function hideOwnLabel() {
    var re = /^[^\w]*[IVX]+\s*·\s*[^—]{1,30}—\s*\d+\s*\/\s*76\b[^\n]{0,40}$/i, all = document.body.getElementsByTagName('*');
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      if (el.children.length > 3 || !re.test(el.textContent)) continue;
      var inner = false;
      for (var j = 0; j < el.children.length; j++) if (re.test(el.children[j].textContent)) inner = true;
      if (inner) continue;
      if (getComputedStyle(el).display === 'inline') el.style.display = 'none';   // no gap left in a line
      else el.style.visibility = 'hidden';                                          // blocks keep the layout
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', hideOwnLabel);
  else hideOwnLabel();
  var css = document.createElement('style');
  css.textContent = 'html.scene-embedded{scrollbar-width:none}html.scene-embedded::-webkit-scrollbar{display:none}';
  document.head.appendChild(css);

  addEventListener('wheel', function (e) {
    if (root.hasAttribute('data-own-wheel')) return;
    e.preventDefault();
    var k = e.deltaMode === 1 ? 16 : e.deltaMode === 2 ? innerHeight : 1;
    post({ t: 'wheel', dy: e.deltaY * k });
  }, { passive: false });

  // Phones: the story moves one section per deliberate flick (index.html "paged" mode).
  // Nothing scrolls while a thumb is down, so holding and dragging always belongs to the
  // scene; only a quick vertical flick lifted within 0.6 s counts as "next" or "previous".
  var coarse = matchMedia('(pointer: coarse)').matches && !matchMedia('(hover: hover)').matches;
  if (coarse) {
    css.textContent += 'html.scene-embedded{touch-action:pan-x pinch-zoom}';
    var fx = 0, fy = null, ft = 0;
    addEventListener('touchstart', function (e) {
      if (e.touches.length !== 1) { fy = null; return; }
      fx = e.touches[0].clientX; fy = e.touches[0].clientY; ft = performance.now();
    }, { passive: true });
    addEventListener('touchend', function (e) {
      if (fy === null) return;
      var t0 = e.changedTouches[0], dy = fy - t0.clientY, dx = fx - t0.clientX, dt = performance.now() - ft;
      fy = null;
      if (Math.abs(dy) > 50 && Math.abs(dy) > Math.abs(dx) * 1.4 && dt < 600) post({ t: 'swipe', dir: dy > 0 ? 1 : -1 });
    }, { passive: true });
  } else if (!root.hasAttribute('data-own-touch')) {
  // Touch without paging (a touch laptop): vertical swipes inside a scene scroll the story.
  // A scene whose own effect needs vertical dragging sets <html data-own-touch>; a scene that
  // calls preventDefault on a touchmove keeps that move.
    css.textContent += 'html.scene-embedded{touch-action:pan-x pinch-zoom}';
    var ty = null, tt = 0, tv = 0;
    addEventListener('touchstart', function (e) {
      if (e.touches.length !== 1) { ty = null; return; }
      ty = e.touches[0].clientY; tt = performance.now(); tv = 0;
    }, { passive: true });
    addEventListener('touchmove', function (e) {
      if (ty === null || e.touches.length !== 1) return;
      var y = e.touches[0].clientY, now = performance.now(), dy = ty - y, dt = Math.max(now - tt, 1);
      ty = y; tt = now;
      setTimeout(function () {                       // after the scene's own listeners ran
        if (e.defaultPrevented) return;
        tv = tv * 0.6 + (dy / dt) * 0.4;
        post({ t: 'touch', dy: dy });
      }, 0);
    }, { passive: true });
    addEventListener('touchend', function () {
      if (ty === null) return;
      ty = null;
      if (Math.abs(tv) > 0.15) post({ t: 'fling', v: tv });
    }, { passive: true });
  }

  var told = false;
  function interacted() { if (!told) { told = true; post({ t: 'interact' }); } }
  addEventListener('pointerdown', interacted, true);
  addEventListener('keydown', interacted, true);

  var KEYS = { ArrowDown: 1, ArrowUp: 1, PageDown: 1, PageUp: 1, ' ': 1, Home: 1, End: 1 };
  addEventListener('keydown', function (e) {
    var el = e.target;
    if (!KEYS[e.key] || /INPUT|TEXTAREA|SELECT/.test(el.tagName) || el.isContentEditable) return;
    if (e.key === ' ' && el.tagName === 'BUTTON') return;
    e.preventDefault();
    post({ t: 'key', k: e.key, shift: e.shiftKey });
  });

  function tone() {
    var bg = getComputedStyle(document.body).backgroundColor;
    if (!bg || bg === 'transparent' || /rgba\(.*,\s*0\)$/.test(bg)) bg = getComputedStyle(root).backgroundColor;
    var m = bg && bg.match(/\d+(\.\d+)?/g);
    if (!m) return;
    var l = (0.2126 * m[0] + 0.7152 * m[1] + 0.0722 * m[2]) / 255;
    if (!root.hasAttribute('data-tone')) S.tone(l > 0.6);
    else S.tone(root.getAttribute('data-tone') === 'light');
  }
  function report() {
    var b = document.body;
    post({ t: 'size', h: Math.max(root.scrollHeight, b ? b.scrollHeight : 0), vh: innerHeight, mode: root.dataset.scene || 'static' });
  }
  addEventListener('load', function () {
    report();
    if (window.ResizeObserver && document.body) new ResizeObserver(report).observe(document.body);
    post({ t: 'ready' });
  });

  addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.salt || e.source !== parent) return;
    if (d.t === 'scroll') {
      if (S.thaw && d.y !== window.scrollY) S.thaw(700, false);   // scroll scenes still follow the scroll
      window.scrollTo(0, d.y);
    }
    else if (d.t === 'progress') dispatchEvent(new CustomEvent('scene:progress', { detail: { p: d.p } }));
    else if (d.t === 'enter') {
      told = false;
      if (S.thaw) S.thaw();
      tone();
      fire();
      if (S.onEnter) S.onEnter();
      dispatchEvent(new Event('scene:enter'));
    } else if (d.t === 'leave') {
      if (S.onLeave) S.onLeave();
      dispatchEvent(new Event('scene:leave'));
    }
  });
})();
