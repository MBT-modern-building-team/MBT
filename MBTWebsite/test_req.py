import requests

s = requests.Session()
# 1. Get CSRF token
r1 = s.get('http://localhost:8000/admin/login/')
print("GET /admin/login/ status:", r1.status_code)
csrf = s.cookies.get('csrftoken')
print("CSRF token:", csrf)

# 2. Login
data = {
    'username': 'admin@mbt.pl',
    'password': 'admin123', # Assuming this isn't correct, but it might be since I reset it in the sandbox DB? Wait, the sandbox DB and user DB are the same db.sqlite3!
    'next': '/admin/',
    'csrfmiddlewaretoken': csrf
}
r2 = s.post('http://localhost:8000/admin/login/', data=data, allow_redirects=False)
print("POST /admin/login/ status:", r2.status_code)
print("Headers:", r2.headers)
print("Cookies:", s.cookies.get_dict())
