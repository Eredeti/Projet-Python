import requests
import folium

class Visualise:
    url_coor = 'https://raw.githubusercontent.com/Eredeti/Projet-Python/main/world_countries.json'
    coordonnees = []  # Variable de classe pour stocker les coordonnées
    
    cord_y = -20
    cord_x = 55
    
    def __init__(self):
        self.coor = self.get_coordinates()
        self.carte = self.get_carte()
        
    def get_coordinates(self):
        response = requests.get(self.url_coor)  # Correction ici, utiliser self.url_coor au lieu de url2
        data = response.json() #Possibilité de le réduire en une seule ligne ???????
        
        for coo in data['features']:
            name = coo['properties']['name']
            coordinates = coo['geometry']['coordinates']
            self.coordonnees.append((name, coordinates))
        return self.coordonnees
    
    def get_carte(self):
        self.map = folium.Map(location=[Visualise.cord_y, Visualise.cord_x], zoom_start=1) # Le zoom en constante ?

        for country, coordinates in self.coor:
            name_country = self.get_name(country)
            for polygon in coordinates:
                vrai_coo = []
                for faux_coo in polygon:
                    if isinstance(faux_coo[0], list):  # Vérifier si c'est une liste de coordonnées
                        for coord in faux_coo:
                            longi, latit = coord
                            vrai_coo.append((latit, longi))
                    else:
                        longi, latit = faux_coo
                        vrai_coo.append((latit, longi))
                folium.PolyLine(vrai_coo, color="red", fill_color="pink", fill_opacity=0.7, tooltip=name_country).add_to(self.map)

        return self.map
    
    def get_name(self, country):
        words = country.split()
        half_length = len(words) // 2
        first_half = " ".join(words[:half_length])  # Joindre la première moitié des mots
        
        return first_half 
# Mettre une def pour diviser le nom en deux 

visual = Visualise() 
carte = visual.carte
carte
