(function () {
  'use strict';

  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.getElementById('nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var open = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    navLinks.addEventListener('click', function (e) {
      if (e.target.closest('a')) navLinks.classList.remove('open');
    });
  }

  var banner = document.getElementById('cookie-banner');
  var accept = document.getElementById('cookie-accept');
  if (banner && accept) {
    var accepted = false;
    try { accepted = localStorage.getItem('kalis-cookie-accepted') === '1'; } catch (e) {}
    if (accepted) {
      banner.classList.add('hidden');
      if (typeof gtag === 'function') {
        gtag('consent', 'update', {
          analytics_storage: 'granted',
          ad_storage: 'granted',
          ad_user_data: 'granted',
          ad_personalization: 'granted'
        });
      }
    } else {
      requestAnimationFrame(function () { banner.classList.remove('hidden'); });
    }
    accept.addEventListener('click', function () {
      banner.classList.add('hidden');
      try { localStorage.setItem('kalis-cookie-accepted', '1'); } catch (e) {}
      if (typeof gtag === 'function') {
        gtag('consent', 'update', {
          analytics_storage: 'granted',
          ad_storage: 'granted',
          ad_user_data: 'granted',
          ad_personalization: 'granted'
        });
      }
    });
  }

  function gaClientId() {
    try {
      var m = document.cookie.match(/(?:^|;\s*)_ga=GA\d+\.\d+\.(\d+\.\d+)/);
      return m ? m[1] : '';
    } catch (e) { return ''; }
  }

  var form = document.getElementById('lead-form');
  if (!form) return;
  var submit = form.querySelector('button[type="submit"]');
  var consent = form.querySelector('input[name="privacy"]');
  var feedback = document.getElementById('form-feedback');
  var market = form.getAttribute('data-market') || '';

  function syncSubmit() {
    if (submit) submit.disabled = !(consent && consent.checked);
  }
  if (consent) consent.addEventListener('change', syncSubmit);
  syncSubmit();

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    if (submit) { submit.disabled = true; submit.textContent = 'Sending…'; }
    if (feedback) { feedback.style.display = 'none'; feedback.className = 'feedback'; }

    var data = new URLSearchParams(new FormData(form));
    data.set('Form_Language', 'en');
    data.set('Form_Page', location.pathname);
    data.set('GA_Client_ID', gaClientId());
    if (market) data.set('market', market);

    fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: data.toString()
    }).then(function (r) {
      return r.json().catch(function () { return { success: false }; });
    }).then(function (resp) {
      if (!resp || resp.success !== true) throw new Error('send failed');
      if (typeof gtag === 'function') {
        gtag('event', 'form_submit', { method: 'geo_landing', market: market });
        gtag('event', 'generate_lead', { method: 'geo_landing', market: market });
      }
      if (feedback) {
        feedback.textContent = 'Thank you. Your inquiry is with us; we will reply by email.';
        feedback.style.display = 'block';
      }
      form.reset();
      syncSubmit();
    }).catch(function () {
      if (feedback) {
        feedback.innerHTML = 'The form did not send. Email <a href="mailto:hello@kalistorik.com">hello@kalistorik.com</a> directly and we will pick it up from there.';
        feedback.className = 'feedback error';
        feedback.style.display = 'block';
      }
      if (submit) submit.disabled = false;
    }).finally(function () {
      if (submit) {
        submit.textContent = 'Send requirements';
        syncSubmit();
      }
    });
  });
})();
