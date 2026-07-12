/* Salt Services — shared script: mobile nav toggle + Coraline form lazy-loader */
(function () {
  'use strict';

  /* ----- Mobile nav toggle ----- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ----- Coraline form lazy-loader -----
     The raw Coraline embed is a ~2085px iframe plus an external script —
     the heaviest thing on any page. We show a styled placeholder and inject
     the real form only when it scrolls near the viewport or is tapped. */
  var mounts = document.querySelectorAll('.coraline-form');
  if (!mounts.length) return;

  var embedJsLoaded = false;

  function loadForm(mount) {
    if (mount.dataset.loaded) return;
    mount.dataset.loaded = 'true';

    var src = mount.dataset.iframeSrc;
    var formId = mount.dataset.formId;
    var height = parseInt(mount.dataset.formHeight, 10) || 900;

    var iframe = document.createElement('iframe');
    iframe.src = src;
    iframe.id = 'inline-' + formId;
    iframe.title = mount.dataset.formName || 'Contact form';
    iframe.style.cssText = 'width:100%;border:none;border-radius:0;min-height:' + height + 'px';
    iframe.setAttribute('data-layout', "{'id':'INLINE'}");
    iframe.setAttribute('data-trigger-type', 'alwaysShow');
    iframe.setAttribute('data-trigger-value', '');
    iframe.setAttribute('data-activation-type', 'alwaysActivated');
    iframe.setAttribute('data-activation-value', '');
    iframe.setAttribute('data-deactivation-type', 'neverDeactivate');
    iframe.setAttribute('data-deactivation-value', '');
    iframe.setAttribute('data-form-name', mount.dataset.formName || '');
    iframe.setAttribute('data-height', String(height));
    iframe.setAttribute('data-layout-iframe-id', 'inline-' + formId);
    iframe.setAttribute('data-form-id', formId);

    mount.innerHTML = '';
    mount.appendChild(iframe);

    if (!embedJsLoaded) {
      embedJsLoaded = true;
      var s = document.createElement('script');
      s.src = mount.dataset.embedJs;
      s.defer = true;
      document.body.appendChild(s);
    }
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          loadForm(entry.target);
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '600px' });
    mounts.forEach(function (m) { io.observe(m); });
  } else {
    mounts.forEach(loadForm);
  }

  mounts.forEach(function (m) {
    var btn = m.querySelector('.coraline-form__load-btn');
    if (btn) btn.addEventListener('click', function () { loadForm(m); });
  });
})();
