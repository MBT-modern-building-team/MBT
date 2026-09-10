import os
import polib

locale_dir = 'Construz/MBTApp/locale'

translations = {
    'en': {
        'Gdzie budujemy?': 'Where do we build?',
        'Zobacz nasze inwestycje na interaktywnej mapie Polski': 'See our investments on the interactive map of Poland',
        'Zobacz projekt': 'View project'
    },
    'de': {
        'Gdzie budujemy?': 'Wo bauen wir?',
        'Zobacz nasze inwestycje na interaktywnej mapie Polski': 'Sehen Sie unsere Investitionen auf der interaktiven Karte von Polen',
        'Zobacz projekt': 'Projekt ansehen'
    },
    'cs': {
        'Gdzie budujemy?': 'Kde stavíme?',
        'Zobacz nasze inwestycje na interaktywnej mapie Polski': 'Podívejte se na naše investice na interaktivní mapě Polska',
        'Zobacz projekt': 'Zobrazit projekt'
    },
    'sk': {
        'Gdzie budujemy?': 'Kde staviame?',
        'Zobacz nasze inwestycje na interaktywnej mapie Polski': 'Pozrite si naše investície na interaktívnej mape Poľska',
        'Zobacz projekt': 'Zobraziť projekt'
    },
    'hu': {
        'Gdzie budujemy?': 'Hol építünk?',
        'Zobacz nasze inwestycje na interaktywnej mapie Polski': 'Tekintse meg beruházásainkat Lengyelország interaktív térképén',
        'Zobacz projekt': 'Projekt megtekintése'
    }
}

for lang, trans_dict in translations.items():
    po_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
    
    if not os.path.exists(po_path):
        print(f"Skipping {lang}, file not found")
        continue
        
    po = polib.pofile(po_path)
    
    for msgid, msgstr in trans_dict.items():
        entry = po.find(msgid)
        if entry:
            entry.msgstr = msgstr
        else:
            entry = polib.POEntry(
                msgid=msgid,
                msgstr=msgstr
            )
            po.append(entry)
            
    po.save(po_path)
    po.save_as_mofile(mo_path)
    print(f"Updated and compiled {lang}")
