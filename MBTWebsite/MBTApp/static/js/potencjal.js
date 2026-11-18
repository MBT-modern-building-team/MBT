/* Potencjał i referencje: filtr realizacji (?sektor=<slug>) + zdarzenia dataLayer. Vanilla, progressive enhancement. */
(function () {
  'use strict';
  var dl = window.dataLayer = window.dataLayer || [];
  var bar = document.getElementById('pot-filter');
  var status = document.getElementById('pot-filter-status');

  function push(o) { try { dl.push(o); } catch (e) {} }

  if (bar) {
    var buttons = [].slice.call(bar.querySelectorAll('button'));
    var groups = [].slice.call(document.querySelectorAll('.pot-group'));
    var slugs = buttons.map(function (b) { return b.getAttribute('data-sector'); });

    var apply = function (slug) {
      if (slugs.indexOf(slug) < 0) slug = 'all';
      buttons.forEach(function (b) {
        b.setAttribute('aria-pressed', b.getAttribute('data-sector') === slug ? 'true' : 'false');
      });
      var shown = 0;
      groups.forEach(function (g) {
        var on = slug === 'all' || g.getAttribute('data-sector') === slug;
        g.hidden = !on;
        if (on) shown += g.querySelectorAll('.pot-proj').length;
      });
      if (status) status.textContent = shown + ' / ' + (document.querySelectorAll('.pot-proj').length);
      return slug;
    };

    var fromUrl = '';
    try { fromUrl = new URLSearchParams(location.search).get('sektor') || ''; } catch (e) {}
    bar.hidden = false;
    apply(fromUrl || 'all');

    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        var slug = apply(b.getAttribute('data-sector'));
        try {
          var u = new URL(location.href);
          if (slug === 'all') u.searchParams.delete('sektor'); else u.searchParams.set('sektor', slug);
          history.replaceState(null, '', u.pathname + u.search + u.hash);
        } catch (e) {}
        push({ event: 'pr_filter', sektor: slug });
      });
    });
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('[data-pr-event]') : null;
    if (a) push({ event: a.getAttribute('data-pr-event') });
  });
})();
