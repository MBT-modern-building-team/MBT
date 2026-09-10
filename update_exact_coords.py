import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'Construz'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import Project

# [longitude, latitude]
kml_data = {
    "InPost sp. z o.o. Oddział Legnica": [16.1811487, 51.1731582],
    "HERZ": [20.0730015, 49.9949198],
    "Browar Zamkowy Racibórz": [18.2200745, 50.0965337],
    "CANPACK Poland - Brzesko": [20.6219206, 49.9771894],
    "Euronova Sp. z o.o. Sp. K.": [20.0861011, 50.0235169],
    "Epco": [18.8759491, 50.3847018],
    "Euro-Trade Magazyn Centralny": [19.8737154, 50.1202424],
    "Grupa Kapitałowa PUMAR": [19.0131504, 50.3232916],
    "Sutco Polska Sp. z o.o.": [19.0571593, 50.2559561],
    "Kompania Piwowarska S.A.": [16.9971062, 52.3853423],  # Poznań
    "Browar Tychy": [18.9865084, 50.1329145],  # Tychy
    "Less Mess Modlińska": [20.9503183, 52.3437589],
    "Huber+Suhner Polatis": [19.685079, 50.1304881],
    "ATT Kokotów": [20.0948933, 50.0199155],
    "Eurosleeve S.A.": [18.8076197, 50.3461723],
    "Stokado Warszawa Lazurowa": [20.895744, 52.2177584],
    "Fronton Kraków": [19.9411511, 50.075889],
    "Stokado Kraków Nowohucka": [20.0025483, 50.0621679],
    "Venus": [20.0895646, 50.03319],
    "PONAR Wadowice": [18.8517032, 50.1494206],
    "Bater Sp. z o.o.": [18.7209159, 50.2689683],
    "Instalacje Elektryczne Fiołka": [18.2342209, 50.0974579],
    "Vesuvius Poland Sp. z o.o.": [19.8201712, 49.9782175],
    "Fabryka Park": [18.9753366, 50.214195],
    "Brembo Poland Sp. z o.o.": [19.2671997, 50.3592777],
    "Kolejarska": [21.0761354, 52.2917104],
    "Remondis": [18.7844657, 50.4563293],
    "Warmet": [21.5111711, 52.6153422],
    "KOIMEX Zielona Góra": [15.4178416, 51.9825434],
    "Park Handlowy Scallier": [18.8264414, 50.2963029],
    "Ecowipes": [20.7349408, 52.4305024],
    "Less Mess Gdańsk": [18.5456996, 54.3445279],
    "Wessper": [20.5066441, 50.0019853]
}

# DB ID -> KML key
mapping = {
    1: "Kompania Piwowarska S.A.", # Browar Lech Poznań
    2: "CANPACK Poland - Brzesko",
    3: "Bater Sp. z o.o.",
    5: "Venus",
    6: "Sutco Polska Sp. z o.o.",
    7: "InPost sp. z o.o. Oddział Legnica",
    8: "Less Mess Modlińska", # Less Mess Warszawa
    9: "Euronova Sp. z o.o. Sp. K.",
    10: "Euro-Trade Magazyn Centralny",
    12: "HERZ",
    13: "Browar Zamkowy Racibórz",
    14: "Epco",
    15: "CANPACK Poland - Brzesko", # CanPack BSS LAB Brzesk
    17: "Grupa Kapitałowa PUMAR",
    18: "Park Handlowy Scallier",
    19: "Vesuvius Poland Sp. z o.o.",
    20: "Stokado Warszawa Lazurowa", # Stokado Bemowo
    21: "Eurosleeve S.A.",
    22: "Fronton Kraków",
    23: "Huber+Suhner Polatis",
    24: "ATT Kokotów",
    25: "Stokado Kraków Nowohucka",
    29: "Browar Tychy", # Kompania Piwowarska Tychy
    31: "Instalacje Elektryczne Fiołka",
    32: "Fabryka Park",
    33: "Ecowipes",
    35: "Warmet",
    36: "KOIMEX Zielona Góra",
    38: "Wessper",
    39: "PONAR Wadowice"
}

for project_id, kml_key in mapping.items():
    try:
        p = Project.objects.get(id=project_id)
        if kml_key in kml_data:
            p.longitude = kml_data[kml_key][0]
            p.latitude = kml_data[kml_key][1]
            p.save()
            print(f"Updated {p.title} -> {kml_key}")
        else:
            print(f"KEY NOT FOUND: {kml_key}")
    except Project.DoesNotExist:
        print(f"PROJECT NOT FOUND: ID {project_id}")

print("Done mapping.")
