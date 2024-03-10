import requests
import pandas as pd
import folium

class Donnees:
    def __init__(self, key, don1, don2):
        self.key = str(key)
        self.don1 = int(don1)
        self.don2 = int(don2)
    
    def __str__(self):
        return f"Clé: {self.key}, Coût: {self.don1}, Nb joueur : {self.don2}"
    
    def ratio(self):
        # Récupération des données géographiques des États-Unis depuis GitHub
        state_geo = requests.get(
            "https://raw.githubusercontent.com/Eredeti/Projet-Python/main/world_countries.json"
        ).json()

        # Lecture des données à partir du fichier CSV sur GitHub
        state_data = pd.read_csv("https://raw.githubusercontent.com/Eredeti/Projet-Python/main/Top_country.csv")

        # Calcul du ratio d'investissement par joueur
        state_data["Ratio"] = state_data["Gain_Earn"]/state_data["Players"]

        # Création de la carte Folium
        m = folium.Map(location=[48, -102], zoom_start=1)

        # Ajout de la choroplèthe à la carte
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=state_data,
            columns=["Country", "Ratio"],
            key_on="feature.properties.name",
            nan_fill_color="White",
            fill_color="Purples",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Ratio argent gagné / joueur",
        ).add_to(m)

        # Ajout du contrôle des calques à la carte
        folium.LayerControl().add_to(m)

        return m
    
# Instanciation d'un objet Donnees avec des valeurs arbitraires
donnees_esports = Donnees("example", 1000, 500)

# Appel de la méthode ratio() sur l'instance de Donnees
carte_folium = donnees_esports.ratio()

carte
