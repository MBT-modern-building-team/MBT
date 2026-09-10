html_path = 'Construz/MBTApp/templates/oznakowanie/panel.html'
with open(html_path, 'r') as f:
    html = f.read()

js_old = """                .then(blob => {
                    const url = URL.createObjectURL(blob);
                    previewBox.innerHTML = '<img src="' + url + '" alt="Podgląd">';
                })"""

js_new = """                .then(blob => {
                    const url = URL.createObjectURL(blob);
                    if (blob.type === 'application/pdf') {
                        previewBox.innerHTML = '<iframe src="' + url + '#toolbar=0&navpanes=0&scrollbar=0" width="100%" height="240" frameborder="0"></iframe>';
                    } else {
                        previewBox.innerHTML = '<img src="' + url + '" alt="Podgląd">';
                    }
                })"""

if js_old in html:
    html = html.replace(js_old, js_new)
    with open(html_path, 'w') as f:
        f.write(html)
    print("JS updated successfully.")
else:
    print("Could not find JS block to update.")
