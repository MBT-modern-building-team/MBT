import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from django.test import Client

client = Client()

LANGS = ['en', 'de', 'cs', 'sk', 'hu', 'uk']

PRIORITY_SERVICES = [
    'hale-przemyslowe',
    'hale-magazynowe',
    'obiekty-komercyjne',
    'kontakt',
    'oferta',
    'generalne-wykonawstwo',
]

REALIZATION_SLUGS = [
    'ecowipes-nowy-dwor-mazowiecki',
    'less-mess-gdansk',
    'ponar-wadowice',
    'raben',
    'wessper',
]

POLISH_LEAK_PHRASES = [
    "Z pasją budujemy Wasze biznesy. Jeden team – pełna realizacja. Od projektu aż po dach!",
    "Realizacja prowadzona przez MBT Modern Building Team w formule generalnego wykonawstwa.",
    "Szukasz generalnego wykonawcy? Sprawdź nasze realizacje.",
    "Generalny Wykonawca Hal i Obiektów Przemysłowych",
    "Generalny Wykonawca Budowlany - MBT - Śląsk, Kraków, Małopolska",
    "Generalny Wykonawca Hal Przemysłowych i Produkcyjnych - Projektowanie i Budowa - MBT",
    "Budowa Hal Magazynowych i Centrów Logistycznych - Projekt Magazynu - MBT",
    "Budowa Obiektów Handlowych - Projektowanie Hal Komercyjnych - MBT",
]

def check_url(url, lang):
    response = client.get(url, follow=True)
    if response.status_code != 200:
        return False, f"HTTP {response.status_code}"
    
    html = response.content.decode('utf-8')
    leaks = []
    for phrase in POLISH_LEAK_PHRASES:
        if phrase in html:
            leaks.append(phrase[:45] + "...")
    
    return True, leaks

def run_verification():
    print("=================================================================")
    print("STARTING FULL TRANSLATION VERIFICATION ACROSS ALL LANGUAGES")
    print("=================================================================\n")

    total_checks = 0
    passed_checks = 0
    failed_checks = 0

    # 1. Homepage checks
    print("--- 1. HOMEPAGE CHECKS ---")
    for lang in LANGS:
        url = f"/{lang}/"
        ok, leaks = check_url(url, lang)
        total_checks += 1
        if ok and not leaks:
            passed_checks += 1
            print(f"  [OK] {url}")
        else:
            failed_checks += 1
            print(f"  [FAIL] {url} -> Status: {ok}, Leaks: {leaks}")

    # 2. Priority Services & Contact & Offers
    print("\n--- 2. PRIORITY SERVICE & CONTACT PAGES ---")
    for svc in PRIORITY_SERVICES:
        for lang in LANGS:
            url = f"/{lang}/{svc}/"
            ok, leaks = check_url(url, lang)
            total_checks += 1
            if ok and not leaks:
                passed_checks += 1
                print(f"  [OK] {url}")
            else:
                failed_checks += 1
                print(f"  [FAIL] {url} -> Status: {ok}, Leaks: {leaks}")

    # 3. Realizations
    print("\n--- 3. TARGET REALIZATION PAGES ---")
    for slug in REALIZATION_SLUGS:
        for lang in LANGS:
            url = f"/{lang}/realizacja/{slug}/"
            ok, leaks = check_url(url, lang)
            total_checks += 1
            if ok and not leaks:
                passed_checks += 1
                print(f"  [OK] {url}")
            else:
                failed_checks += 1
                print(f"  [FAIL] {url} -> Status: {ok}, Leaks: {leaks}")

    # 4. Blog Details Check
    print("\n--- 4. BLOG DETAILS CHECK ---")
    from MBTApp.models import Article
    sample_article = Article.objects.first()
    if sample_article:
        for lang in LANGS:
            url = f"/{lang}/blog/{sample_article.slug}/"
            ok, leaks = check_url(url, lang)
            total_checks += 1
            if ok and not leaks:
                passed_checks += 1
                print(f"  [OK] {url}")
            else:
                failed_checks += 1
                print(f"  [FAIL] {url} -> Status: {ok}, Leaks: {leaks}")

    print("\n=================================================================")
    print(f"RESULTS: {passed_checks}/{total_checks} passed, {failed_checks} failed.")
    print("=================================================================")

if __name__ == '__main__':
    run_verification()
