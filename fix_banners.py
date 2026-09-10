import os

views_path = 'Construz/MBTApp/oznakowanieViews.py'
urls_path = 'Construz/MBTApp/urls.py'
html_path = 'Construz/MBTApp/templates/oznakowanie/panel.html'

# 1. Update urls.py (remove upload)
with open(urls_path, 'r') as f:
    urls = f.read()
urls = urls.replace("path('admin-budowa/upload/<slug:slug>/', oznakowanieViews._upload_logo_view, name='oznakowanie_upload'),\n    ", "")
with open(urls_path, 'w') as f:
    f.write(urls)

# 2. Update panel.html
with open(html_path, 'r') as f:
    html = f.read()

import re

# Fix general preview icons
html = html.replace(
    '<img src="{{ t.template_image.url }}" alt="Podgląd">',
    '''{% if ".pdf" in t.template_image.name|lower %}
                        <div style="font-size:3rem; padding: 2rem;">📄</div>
                        <div style="font-size:0.8rem; color:#6e6e73; margin-top:0.5rem; margin-bottom: 2rem;">Podgląd PDF niedostępny</div>
                    {% else %}
                        <img src="{{ t.template_image.url }}" alt="Podgląd">
                    {% endif %}'''
)

# Fix personalized form
personalized_old = '''<form class="logo-form" data-slug="{{ t.slug }}">
                    {% csrf_token %}
                    <div class="form-row">
                        <div class="file-input-wrap">
                            <span class="file-label">📁 {% trans "Wybierz logo" %} (PNG/JPG/SVG)</span>
                            <input type="file" name="logo" accept="image/png,image/jpeg,image/svg+xml,image/webp" required>
                        </div>
                        <button type="submit" class="btn btn-blue">{% trans "Wgraj" %}</button>
                    </div>
                </form>

                <div style="display:flex; gap:0.5rem;">
                    <a class="btn btn-blue" style="flex:1" id="dl-{{ t.slug }}" disabled>{% trans "Pobierz baner" %}</a>
                </div>'''

personalized_new = '''<form class="logo-form" data-slug="{{ t.slug }}" method="POST" action="/admin-budowa/pobierz/{{ t.slug }}/" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="form-row">
                        <div class="file-input-wrap">
                            <span class="file-label">📁 {% trans "Wybierz logo" %}</span>
                            <input type="file" name="logo" accept="image/png,image/jpeg,image/svg+xml,image/webp" required>
                        </div>
                        <button type="button" class="btn btn-blue btn-preview">Podgląd</button>
                    </div>
                    <div style="display:flex; gap:0.5rem; margin-top:0.5rem;">
                        <button type="submit" class="btn btn-cta" style="flex:1; width:100%;">{% trans "Pobierz baner" %}</button>
                    </div>
                </form>'''

html = html.replace(personalized_old, personalized_new)

# Fix JS
js_old = '''    <script>
    (function() {
        // Logo upload + preview
        document.querySelectorAll('.logo-form').forEach(function(form) {
            const slug = form.dataset.slug;
            const preview = document.getElementById('preview-' + slug);
            const downloadBtn = document.getElementById('dl-' + slug);
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                const fd = new FormData(form);
                fetch('/admin-budowa/upload/' + slug + '/', {
                    method: 'POST',
                    body: fd,
                    headers: { 'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value },
                    credentials: 'same-origin',
                }).then(r => r.json()).then(d => {
                    if (d.ok) {
                        preview.innerHTML = '<img src="/admin-budowa/podglad/' + slug + '/?t=' + Date.now() + '" alt="preview">';
                        downloadBtn.setAttribute('href', '/admin-budowa/pobierz/' + slug + '/');
                        downloadBtn.removeAttribute('disabled');
                        downloadBtn.classList.remove('btn-blue');
                        downloadBtn.classList.add('btn-cta');
                    } else {
                        alert(d.error || 'Błąd');
                    }
                });
            });
        });
    })();
    </script>'''

js_new = '''    <script>
    (function() {
        document.querySelectorAll('.logo-form').forEach(function(form) {
            const slug = form.dataset.slug;
            const previewBtn = form.querySelector('.btn-preview');
            const previewBox = document.getElementById('preview-' + slug);
            
            // Preview logic
            previewBtn.addEventListener('click', function() {
                const fileInput = form.querySelector('input[type="file"]');
                if (!fileInput.files.length) {
                    alert('Wybierz najpierw plik logo!');
                    return;
                }
                const fd = new FormData(form);
                previewBox.innerHTML = '<div class="ozn-preview-empty">Ładowanie podglądu...</div>';
                
                fetch('/admin-budowa/podglad/' + slug + '/', {
                    method: 'POST',
                    body: fd,
                })
                .then(r => {
                    if (!r.ok) throw new Error('Błąd podglądu');
                    return r.blob();
                })
                .then(blob => {
                    const url = URL.createObjectURL(blob);
                    previewBox.innerHTML = '<img src="' + url + '" alt="Podgląd">';
                })
                .catch(err => {
                    previewBox.innerHTML = '<div class="ozn-preview-empty">Błąd generowania podglądu.</div>';
                });
            });
            
            // File input label update
            form.querySelector('input[type="file"]').addEventListener('change', function(e) {
                const label = form.querySelector('.file-label');
                if (this.files.length) {
                    label.textContent = 'Wybrano: ' + this.files[0].name;
                } else {
                    label.textContent = '📁 Wybierz logo';
                }
            });
        });
    })();
    </script>'''

html = html.replace(js_old, js_new)

with open(html_path, 'w') as f:
    f.write(html)
