import folium
import requests
import csv
import json

class Region:
    
    def __init__(self, pays):
        self.pays = pays
        self.data = self.get_data()      # Appeler toutes les informations du fichier json
        self.coos = self.get_coos()      # Prendre la liste de coordoonnées dans le fichier json
        self.forme = self.get_forme()     # Polygon ou Multipolygon dans le fichier json

        def get_data(self): #
            response = requests.get(Visualise.url_json)
            data = response.json()
            return data

        def get_forme(self):
            for infos in self.data['features']:
                if self.pays == infos['properties']['name']:
                    return infos['geometry']['type']
            return None
        
        def get_coos(self):
            for feature in self.data['features']:
                if pays in feature['properties']['name']:     # Vérifier si le nom du pays correspond à celui recherché
                    coordonnees = feature['geometry']['coordinates']       # Extraire les coordonnées géographiques  
                    coord=[]

                    if self.forme == "Polygon": # Pour retirer une liste inutile
                        coor = coordonnees[0]
                        for i in range (len(coor)):
                            longi, latit = coor[i]
                            coord.append((latit, longi))

                    else :
                        for coo1 in coordonnees:
                            for coo2 in coo1:
                                for i in range (len(coo2)):
                                    longi, latit = coo2[i]
                                    coord.append((latit, longi)) 
                return coord
            return None

class Pays:
    
    def __init__(self, annee, pays):
        
        self.taille = self.get_taille()  # pour connaitre le nb de lignes dans le fichier csv, prend en compte aussi le titre
        self.forme = Region(self.pays).forme
        self.coord = Region(self.pays).coos
        self.annee = annee
        
        self.ratio =     # Parcourir le fichier csv selon le self.pays
        self.pays = pays
        
        self.class =     # Avoir la liste des 10 premiers pour les marqueurs
        self.top =     # Avoir le premier du self.ratio
        
        self.nbr = 

        
        def get_taille(self): # pour connaitre le nombre de pays
            response = requests.get(Visualisation.url_csv)
            lines = response.text.splitlines()  # Utilisation de splitlines() pour diviser les lignes
            return len(list(lines))

        
class Visualisation:    
    cord_y = -20
    cord_x = 55
    zoom = 1
    
    def __init__(self, annee):
        self.annee = annee
        
        self.carte = folium.Map(location=[Visualisation.cord_y, Visualisation.cord_x], zoom_start=Visualisation.zoom)         
        
        self.opacite = Pays().ratio/Pays().top
        self.marqueur = 
        
        self.url_csv = 'https://raw.githubusercontent.com/Eredeti/Projet-Python/main/Top_country_{self.annee}.csv'
        self.url_json = 'https://raw.githubusercontent.com/Eredeti/Projet-Python/main/world_countries.json'
