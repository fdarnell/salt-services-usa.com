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

  /* The SALT AI chat widget ran on Coraline's Conversation AI. Franklin
     retired it with Coraline (2 October 2026): nothing replaces it, and the
     contact form and phone number are the ways in. */

  /* ----- Coraline form lazy-loader -----
     The raw Coraline embed is a ~2085px iframe plus an external script —
     the heaviest thing on any page. We show a styled placeholder and inject
     the real form only when it scrolls near the viewport or is tapped. */
  /* ---- Salt CRM form (replaces Coraline) ----
     Each Coraline form on this site has a twin in Salt CRM, keyed here by the
     Coraline form id the page already carries. A listed mount gets the CRM
     form instead of the iframe: plain HTML rendered into the page, styled by
     this site's CSS, as tall as its content. The embed script mounts every
     CRM form on the page not yet mounted, so it is added again for each. */
  var SALTCRM_FORMS = { 'ZG2GvC7Xk9bF3bCMCEB1': 'H-Diwo9Ic3o7tC2gdugZ1A' };
  var loadSaltcrmForm = function (mount, token) {
    var host = document.createElement('div');
    host.setAttribute('data-saltcrm-form', token);
    mount.innerHTML = '';
    mount.style.minHeight = '';
    mount.classList.add('saltcrm-mount');
    mount.appendChild(host);
    var s = document.createElement('script');
    s.src = 'https://crm.saltservicesusa.com/api/embed/' + token;
    s.async = true;
    document.body.appendChild(s);
  };

  var mounts = document.querySelectorAll('.coraline-form');
  if (!mounts.length) return;

  var embedJsLoaded = false;

  function loadForm(mount) {
    if (mount.dataset.loaded) return;
    mount.dataset.loaded = 'true';
    if (SALTCRM_FORMS[mount.dataset.formId]) { loadSaltcrmForm(mount, SALTCRM_FORMS[mount.dataset.formId]); return; }

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
