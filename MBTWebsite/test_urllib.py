import urllib.request
import urllib.parse
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. Get CSRF token
r1 = opener.open('http://127.0.0.1:8000/admin/login/')
print("GET status:", r1.getcode())
csrf = ""
for c in cj:
    if c.name == 'csrftoken':
        csrf = c.value
print("CSRF:", csrf)

# 2. Login
data = urllib.parse.urlencode({
    'username': 'admin@mbt.pl',
    'password': 'admin123',
    'next': '/admin/',
    'csrfmiddlewaretoken': csrf
}).encode('utf-8')

req = urllib.request.Request('http://127.0.0.1:8000/admin/login/', data=data)
try:
    r2 = opener.open(req)
    print("POST status:", r2.getcode())
    print("URL:", r2.geturl())
except Exception as e:
    print("Exception:", getattr(e, 'code', e))

for c in cj:
    print(c.name, "=", c.value)
