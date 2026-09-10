import urllib.request
import urllib.parse
import json

def translate(text):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": "pl|uk"
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{url}?{query_string}"
    
    req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                print("MyMemory:", data['responseData']['translatedText'])
    except Exception as e:
        print("Error:", e)

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "pl",
        "tl": "uk",
        "dt": "t",
        "q": text
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{url}?{query_string}"
    req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                print("GTX:", data[0][0][0])
    except Exception as e:
        print("GTX Error:", e)

translate("Cześć, jak się masz?")
