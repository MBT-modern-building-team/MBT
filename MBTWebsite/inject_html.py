html_to_inject = """
        <h2 style="margin-top: 3rem; color: #1d1d1f;">{% trans "Tablice Budowlane (Generatory)" %}</h2>
        <div class="ozn-grid">
            <!-- TABLICA BIOZ -->
            <div class="ozn-card">
                <h2>Tablica (Ogłoszenie) BIOZ</h2>
                <div class="size">70 x 70 cm</div>

                <div class="ozn-preview" id="preview-bioz">
                    <div class="ozn-preview-empty">Wypełnij formularz i kliknij Podgląd</div>
                </div>

                <form class="board-form" data-type="bioz" method="POST" action="{% url 'board_download' 'bioz' %}">
                    {% csrf_token %}
                    <div class="form-row" style="flex-direction: column; align-items: stretch; gap: 0.5rem; margin-top: 1rem;">
                        <input type="text" name="rozpoczecie" placeholder="ROZPOCZĘCIE ROBÓT" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="zakonczenie" placeholder="ZAKOŃCZENIE ROBÓT" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="maks_prac" placeholder="MAKS. LICZBA PRACOWNIKÓW NA BUDOWIE" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="plan_bioz" placeholder="PLAN BEZPIECZEŃSTWA ZNAJDUJE SIĘ..." required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                    </div>
                    <div style="display:flex; gap:0.5rem; margin-top:1rem;">
                        <button type="button" class="btn btn-blue btn-preview-board">Podgląd</button>
                        <button type="submit" class="btn btn-cta" style="flex:1;">Pobierz PDF</button>
                    </div>
                </form>
            </div>

            <!-- TABLICA INFORMACYJNA -->
            <div class="ozn-card">
                <h2>Tablica Informacyjna</h2>
                <div class="size">70 x 103 cm</div>

                <div class="ozn-preview" id="preview-informacyjna">
                    <div class="ozn-preview-empty">Wypełnij formularz i kliknij Podgląd</div>
                </div>

                <form class="board-form" data-type="informacyjna" method="POST" action="{% url 'board_download' 'informacyjna' %}">
                    {% csrf_token %}
                    <div class="form-row" style="flex-direction: column; align-items: stretch; gap: 0.5rem; margin-top: 1rem;">
                        <input type="text" name="budowa" placeholder="BUDOWA" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="adres" placeholder="ADRES" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="data_pozwolenia" placeholder="DATA I NR POZWOLENIA/ZGŁOSZ." required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="organ" placeholder="ORGAN WYD. DEC./ROZP.ZGŁOSZ." required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="nadzor" placeholder="NADZÓR BUDOWLANY" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="inwestor" placeholder="INWESTOR" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                        <input type="text" name="kierownik" placeholder="KIEROWNIK BUDOWY" required style="padding:0.5rem; border:1px solid #ccc; border-radius:4px;">
                    </div>
                    <div style="display:flex; gap:0.5rem; margin-top:1rem;">
                        <button type="button" class="btn btn-blue btn-preview-board">Podgląd</button>
                        <button type="submit" class="btn btn-cta" style="flex:1;">Pobierz PDF</button>
                    </div>
                </form>
            </div>
        </div>
"""

js_to_inject = """
            // Dodana logika dla formularzy tablic budowlanych
            document.querySelectorAll('.board-form').forEach(function(form) {
                const bType = form.dataset.type;
                const previewBtn = form.querySelector('.btn-preview-board');
                const previewBox = document.getElementById('preview-' + bType);
                
                previewBtn.addEventListener('click', function() {
                    const fd = new FormData(form);
                    previewBox.innerHTML = '<div class="ozn-preview-empty">Generowanie...</div>';
                    
                    fetch('/admin-budowa/tablice/' + bType + '/podglad/', {
                        method: 'POST',
                        body: fd,
                    })
                    .then(r => {
                        if (!r.ok) throw new Error('Błąd podglądu');
                        return r.blob();
                    })
                    .then(blob => {
                        const url = URL.createObjectURL(blob);
                        previewBox.innerHTML = '<iframe src="' + url + '#toolbar=0&navpanes=0&scrollbar=0&view=Fit" width="100%" height="300" frameborder="0"></iframe>';
                    })
                    .catch(err => {
                        previewBox.innerHTML = '<div class="ozn-preview-empty">Błąd generowania podglądu.</div>';
                    });
                });
            });
"""

with open('MBTApp/templates/oznakowanie/panel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert HTML after personalized banners
if "<!-- TABLICE INJECT -->" not in content:
    target_html = "{% if my_downloads %}"
    content = content.replace(target_html, html_to_inject + "\n        " + target_html, 1)

    # Insert JS
    target_js = "// Preview logic"
    content = content.replace(target_js, js_to_inject + "\n            " + target_js, 1)

    with open('MBTApp/templates/oznakowanie/panel.html', 'w', encoding='utf-8') as f:
        f.write(content)
