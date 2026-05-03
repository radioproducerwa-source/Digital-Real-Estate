/* Perth Bond Clean — main.js */

// ── Mobile nav ──
const hamburger = document.getElementById('hamburger');
const mainNav   = document.getElementById('main-nav');

if (hamburger && mainNav) {
  hamburger.addEventListener('click', () => {
    const open = mainNav.classList.toggle('open');
    hamburger.textContent = open ? '✕' : '☰';
    hamburger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  mainNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mainNav.classList.remove('open');
      hamburger.textContent = '☰';
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });
}

// ── Suburbs dropdown (desktop) ──
document.querySelectorAll('.dropdown').forEach(dd => {
  const btn  = dd.querySelector('.dropdown-btn');
  const menu = dd.querySelector('.dropdown-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', e => {
    e.stopPropagation();
    menu.classList.toggle('open');
  });
  document.addEventListener('click', () => menu.classList.remove('open'));
});

// ── FAQ accordion ──
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    // close all
    document.querySelectorAll('.faq-item.open').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
    });
    if (!isOpen) {
      item.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});

// ── Form submit (Formspree AJAX) ──
document.querySelectorAll('form[data-formspree]').forEach(form => {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;
    btn.disabled = true;
    btn.textContent = 'Sending…';

    const successId = form.dataset.successId || 'form-success';
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      });
      if (res.ok) {
        form.style.display = 'none';
        const success = document.getElementById(successId);
        if (success) { success.removeAttribute('hidden'); success.style.display = ''; }
      } else {
        btn.textContent = 'Error — please try again';
        btn.disabled = false;
      }
    } catch {
      btn.textContent = 'Error — please try again';
      btn.disabled = false;
      setTimeout(() => { btn.textContent = originalText; }, 3000);
    }
  });
});

// ── Active nav link ──
const path = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.main-nav > a').forEach(a => {
  const href = a.getAttribute('href');
  if (href === path || (path === '' && href === 'index.html')) {
    a.classList.add('active');
  }
});

// ── Footer year ──
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();
