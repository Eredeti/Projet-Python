import csv
import json
noms_pays = []
pays = []

def ouvrir_fichier (fichier1,fichier2):
    with open(fichier2, 'r', encoding='utf-8') as jsonfile:
        ligne = json.load(jsonfile)
    
    for feature in ligne['features']:
        nom_pays = feature['properties']['name']
        noms_pays.append(nom_pays)

    
    with open(fichier1, 'r', newline='', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv, delimiter=',')
        
        for ligne in lecteur_csv:
            colonne_pays=ligne['Country']
            pays.append(colonne_pays)

    for element in pays:
        if element in noms_pays:
            pass
        else:
            print ("Le pays :",element, "n'est pas dans le fichier json")
    

ouvrir_fichier('Top_country.csv','world_countries.json')
