/* ──────────────────────────────────────────────────────────────
 * picks-modal.js
 * Shared modal logic for KALIS TORIK OUR PICKS cards.
 * Used by both index.html (3-card ad grid) and picks.html (hook slides).
 * Depends on a #picks-modal element with the structure:
 *   <div id="picks-modal">
 *     <h2 id="picks-modal-title">…</h2>
 *     <p id="picks-modal-body">…</p>
 *     <a id="picks-modal-cta">…</a>
 *     <button data-modal-close>×</button>
 *   </div>
 * Triggers: any element with [data-modal="hook1|hook2|hook3"].
 * ────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  // === Content (kept verbatim from picks.html for parity) ============
  var MODAL_CONTENT = {
    hook1: {
      title: "We say no to more factories than most sourcing agents ever visit.",
      body:  "A small list, kept that way on purpose. After twenty years, we still walk the floor ourselves.",
      cta:   "Ask us what we'd refuse today",
      href:  "/wa.html"
    },
    hook2: {
      title: "Your first order doesn't need to be perfect. It needs to be real.",
      body:  "Some of our first buyers sent 30 pieces. We sent back photos before the balance. That part doesn't change.",
      cta:   "Talk through your first order",
      href:  "/wa.html"
    },
    hook3: {
      title: "Twenty years on the ground. One person, start to finish.",
      body:  "From the first sample to the container at your port. No team handoff, no rotating rep.",
      cta:   "See how it works",
      href:  "/wa.html"
    }
  };

  // === DOM refs =====================================================
  var modal       = document.getElementById('picks-modal');
  var modalTitle  = document.getElementById('picks-modal-title');
  var modalBody   = document.getElementById('picks-modal-body');
  var modalCTA    = document.getElementById('picks-modal-cta');
  var modalClose  = modal ? modal.querySelector('[data-modal-close]') : null;

  if (!modal) return; // No modal in this page — nothing to wire.

  // === Open / close =================================================
  function openModal(key) {
    var data = MODAL_CONTENT[key];
    if (!data) return;
    if (modalTitle) modalTitle.textContent = data.title;
    if (modalBody)  modalBody.textContent  = data.body;
    if (modalCTA) {
      modalCTA.textContent = data.cta + ' ';
      modalCTA.href        = data.href;
    }
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // === Wire triggers: any [data-modal="hookN"] element ==============
  var triggers = document.querySelectorAll('[data-modal]');
  triggers.forEach(function (el) {
    el.addEventListener('click', function (e) {
      // Don't open if user clicked an inner link/button
      if (e.target.closest('a, button')) return;
      var key = el.getAttribute('data-modal') || el.getAttribute('data-id');
      openModal(key);
    });
  });

  // === Close interactions ===========================================
  if (modalClose) modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', function (e) {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('is-open')) {
      closeModal();
    }
  });
})();
