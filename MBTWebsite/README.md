# MBT — strona firmy Modern Building Team

Stronę internetową MBT (https://mbt.pl) zbudowałem w Django 5.2. Wersja lokalna odwzorowuje
strukturę i treści oryginalnej strony: realizacje, kariera, oferta, blog, o nas, kontakt.

## Szybki start

```bash
# 1. Wejdź do projektu
cd Construz

# 2. Uruchom serwer developerski
.venv/bin/python manage.py runserver 0.0.0.0:8765
```

Strona: http://localhost:8765/

## Struktura projektu

```
Construz/
├── MBT/                  # konfiguracja Django (settings, urls, wsgi)
├── MBTApp/               # aplikacja (widoki, dane, szablony, statyczne)
│   ├── mbt_data.py       # ⭐ WSZYSTKIE DANE STRONY (edytuj tutaj!)
│   ├── context.py        # wstrzykuje dane (site, articles) do szablonów
│   ├── homeViews.py      # strona główna, o nas, kontakt
│   ├── mbtViews.py       # realizacje, kariera, polityka prywatności
│   ├── newsViews.py      # blog, artykuły
│   ├── serviceViews.py   # oferta
│   ├── urls.py           # adresy stron (URL-e)
│   ├── templates/        # szablony HTML
│   └── static/           # CSS, JS, obrazy (img/mbt/ = zdjęcia)
└── manage.py
```

## ⭐ Jak zmienić dane firmy (telefon, adresy, liczniki, social)

Wszystko zebrałem w **jednym pliku**: `MBTApp/mbt_data.py` → sekcja `SITE`:

```python
SITE = {
    'phone': '+48 881 444 333',          # telefon (wszędzie: header, footer, kontakt)
    'email': 'biuro@mbt.pl',
    'office_zabrze': 'Roosevelta 81, 41-800 Zabrze',
    'office_katowice': 'Jankego 176/1A, 40-663 Katowice',
    'office_krakow': 'Zawiła 65, bud. X lok. 5, 30-390 Kraków',
    'counter_years': '20',               # liczniki na stronie głównej
    'counter_projects': '100',
    ...
}
```

Po zmianie **zrestartuj serwer** (Ctrl+C, potem uruchom ponownie).

## Jak podmienić zdjęcia

- Obrazy strony trzymam w: `MBTApp/static/img/mbt/` (np. `o-nas-1.jpg`, `realizacja-eurosleeve.jpg`)
- Każdy projekt w `mbt_data.py` ma pola `hero` (okładka) i `gallery` (lista zdjęć) —
  wskaż tam nazwę pliku, np. `'hero': '/static/img/mbt/moje-zdjecie.jpg'`
- Wystarczy wrzucić plik do folderu `static/img/mbt/` i wpisać jego nazwę w `mbt_data.py`

## Adresy stron (URL-e)

| Opis na stronie | Adres |
|---|---|
| Strona główna | `/` |
| O nas | `/o-nas/` |
| Oferta | `/oferta/` |
| Realizacje (lista, 4 strony) | `/realizacje/` |
| Szczegóły realizacji | `/realizacja/<slug>/` |
| Blog (lista artykułów) | `/blog/` |
| Artykuł | `/blog/<slug>/` |
| Kariera (oferty pracy) | `/kariera/` |
| Szczegóły oferty | `/kariera/<slug>/` |
| Kontakt | `/kontakt/` |
| Polityka prywatności | `/polityka-prywatnosci/` |

## Wdrożenie na Vercel

1. Wypchnij repo na GitHub (`.env` NIE jest commitowany — patrz `.gitignore`).
2. Import projektu w Vercel (Framework Preset: **Other** — konfiguracja jest w `vercel.json`).
3. Ustaw zmienne środowiskowe w **Dashboard → Settings → Environment Variables**:
   - `DJANGO_SECRET_KEY` — wygeneruj np. `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `twoja-domena.vercel.app,admin.twoja-domena.vercel.app`
   - `DATABASE_URL` — adres Postgres (utwórz w Vercel → Storage → Postgres, skopiuj URL)
   - `DJANGO_SUPERUSER_EMAIL` = `m.dziubek@mbt.pl`
   - `DJANGO_SUPERUSER_PASSWORD` = Twoje tajne hasło (do zmiany w panelu po zalogowaniu)
4. Deploy. Pliki statyczne serwuje Vercel z `MBTApp/static/**` (rule w `vercel.json`), cały
   pozostały ruch trafia do `api/index.py` (Django przez `serverless-wsgi`).
   Przy starcie automatycznie: `migrate` + seed danych + utworzenie superusera z env.

> Uwaga: strona nie używa bazy danych (wszystkie treści są w `mbt_data.py`),
> więc `db.sqlite3` nie jest potrzebny na Vercel — nie musi być deployowany.

## 🛠 Panel administracyjny (CMS)

Panel: **https://admin.twoja-domena.vercel.app/admin/** (lub `admin.twoja-domena.pl/admin/`).

- **Subdomena admin.*** — dodaj ją w Vercel: **Settings → Domains → Add** (`admin.…`).
  Middleware przekierowuje każde wejście na `/admin/` z głównej domeny na subdomenę `admin.`.
- **Login:** `m.dziubek@mbt.pl` + hasło (z `DJANGO_SUPERUSER_PASSWORD`).
- **Zmiana hasła:** w panelu, prawy górny róg → „Zmień hasło".
- **Co edytujesz:**
  - *Realizacje* — tytuł, status (zrealizowane/w trakcie), czas, formuła, opis,
    zdjęcie główne (`hero`), logo, galeria (lista URL-i w polu JSON),
    kolejność na liście.
  - *Oferty pracy* — stanowiska w dziale Kariera.
  - *Pracownicy* — zespół (imię, stanowisko, zdjęcie).
  - *Opinie klientów* — referencje.
  - *Artykuły* — blog (tytuł, skrót, treść, zdjęcie, opublikowany ✓).
  - *Dane firmy* — telefon, adresy biur, liczniki, NIP/REGON/KRS, social media
    (jeden rekord — edytujesz wszystko w jednym miejscu).
- **Zdjęcia:** pole przyjmuje pełny URL (https://…) LUB ścieżkę `/static/img/mbt/…`
  dla plików wgranych do projektu. Aby wrzucić nowe zdjęcie z dysku — wgraj je
  do `MBTApp/static/img/mbt/`, commit + push, potem wpisz nazwę w adminie.

## Dane projektu / ofert pracy / artykułów

Wszystkie treści (25 realizacji, oferty pracy, pracownicy, artykuły, opinie klientów)
umieściłem w `MBTApp/mbt_data.py` — sekcje: `PROJECTS`, `JOBS`, `WORKERS`,
`REFERENCES`, `ARTICLES`. Każdy wpis to słownik z polami `title`, `slug`, `opis` itd.
Aby dodać nową realizację, skopiuj istniejący wpis i zmień pola (slug musi być unikalny).

## O projekcie

Całość zaprogramowałem z myślą o prostocie zarządzania i łatwości wdrożenia na darmowy hosting (Vercel).
Kod napisałem samodzielnie, dbając o czystość i czytelność.
