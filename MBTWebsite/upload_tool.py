import os
import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleUploadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <html>
        <head><title>Wgrywanie plików dla AI</title></head>
        <body style="font-family: sans-serif; margin: 40px; line-height: 1.6;">
            <h2>Wgraj pliki do generowania tablic budowlanych</h2>
            <p>Użyj poniższego formularza, aby przekazać mi (AI) potrzebne pliki. Zapiszę je automatycznie w odpowiednich folderach Twojego projektu Django.</p>
            <form enctype="multipart/form-data" method="POST" style="background: #f4f4f4; padding: 20px; border-radius: 8px;">
                <p><b>1. Szablon: Tablica informacyjna</b> (PNG/JPG):</p>
                <input type="file" name="tablica_inf" required>
                <br><br>
                <p><b>2. Szablon: Tablica BIOZ</b> (PNG/JPG):</p>
                <input type="file" name="tablica_bioz" required>
                <br><br>
                <p><b>3. Czcionka</b> (np. SF-Pro-Compressed-Heavy.ttf lub .otf):</p>
                <input type="file" name="czcionka" required>
                <br><br><hr><br>
                <input type="submit" value="Wgraj pliki na serwer!" style="padding: 10px 20px; font-size: 16px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_type = self.headers.get('Content-Type')
        if not content_type:
            return
        
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     }
        )

        media_dir = "/Users/marek-macbook/MBT/nowa strona/MBTWebsite/media"
        os.makedirs(f"{media_dir}/tablice_szablony", exist_ok=True)
        os.makedirs(f"{media_dir}/fonts", exist_ok=True)

        msg = "<body style='font-family: sans-serif; margin: 40px;'><h3>Pliki wgrane pomyślnie!</h3><ul>"

        for field, folder in [('tablica_inf', 'tablice_szablony'), 
                              ('tablica_bioz', 'tablice_szablony'), 
                              ('czcionka', 'fonts')]:
            if field in form and form[field].filename:
                item = form[field]
                filepath = os.path.join(media_dir, folder, os.path.basename(item.filename))
                with open(filepath, 'wb') as f:
                    f.write(item.file.read())
                msg += f"<li>Zapisano: <b>{item.filename}</b> (w folderze media/{folder}/)</li>"

        msg += "</ul><p style='color: green;'><b>Gotowe! Możesz zamknąć tę zakładkę i napisać do mnie w czacie AI, że pliki zostały wgrane.</b></p></body>"

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(msg.encode("utf-8"))

server = HTTPServer(('localhost', 8888), SimpleUploadHandler)
print("Serwer dziala na http://localhost:8888")
server.serve_forever()
