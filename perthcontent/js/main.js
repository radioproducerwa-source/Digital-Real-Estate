/* =========================================================
   Perth Content — Main JS
   ========================================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* --- Mobile hamburger --------------------------------- */
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('main-nav');

  if (hamburger && nav) {
    hamburger.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);
    });

    // Close nav when a link is clicked
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --- Mobile dropdown toggle --------------------------- */
  document.querySelectorAll('.dropdown-btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      // Only toggle on mobile
      if (window.innerWidth <= 720) {
        e.preventDefault();
        const parent = btn.closest('.dropdown');
        parent.classList.toggle('open');
      }
    });
  });

  /* --- FAQ accordion ------------------------------------ */
  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      // Close all
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        openItem.classList.remove('open');
      });

      // Open clicked if it was closed
      if (!isOpen) { item.classList.add('open'); }
    });
  });

  /* --- Smooth scroll for anchor links ------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* --- Active nav link ---------------------------------- */
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav > a').forEach(function (link) {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentPath) {
      link.style.color = '#0ea5e9';
    }
  });

});
