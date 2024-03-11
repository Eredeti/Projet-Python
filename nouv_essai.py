import csv
import json

def mots_dans_autre_fichier_csv_json(csv_file, json_file):
    # Ouvre le fichier CSV en mode lecture
    with open(csv_file, 'r', newline='') as csv_f:
        csv_reader = csv.reader(csv_f)
        mots_fichier_csv = set(row[0] for row in csv_reader if row)

    # Ouvre le fichier JSON en mode lecture
    with open(json_file, 'r') as json_f:
        data = json.load(json_f)
        if isinstance(data, list):  # Vérifie si le fichier JSON est une liste
            mots_fichier_json = set(data)
        else:
            raise ValueError("Le fichier JSON doit contenir une liste de mots.")

    # Vérifie si les mots du fichier JSON sont présents dans le fichier CSV
    mots_absents = mots_fichier_json - mots_fichier_csv
    if mots_absents:
        print("Les mots suivants dans le fichier JSON ne sont pas présents dans le fichier CSV :")
        for mot in mots_absents:
            print(mot)
    else:
        print("Tous les mots du fichier JSON sont présents dans le fichier CSV.")

# Utilisation de la fonction avec un fichier CSV et un fichier JSON comme arguments
mots_dans_autre_fichier_csv_json("Top_country.csv", "world_countries.json")
