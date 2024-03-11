import requests
import pandas as pd
import folium

class Esport:
    def __init__(self,annee,classement):
        self.annee = str(annee)
        self.classement = int(classement)
    
    def __str__(self):
        pass 
    
    def ratio(self):
        # Récupération des données géographiques des pays depuis Github
        state_geo = requests.get(
            "https://raw.githubusercontent.com/Eredeti/Projet-Python/main/world_countries.json"
        ).json()

        url = f"https://raw.githubusercontent.com/Eredeti/Projet-Python/main/Top_country_{self.annee}.csv"
        
        # Lecture des données à partir du fichier CSV sur GitHub
        state_data = pd.read_csv(url)

        # Calcul du ratio d'investissement par joueur
        state_data["Ratio"] = state_data["Gain_Earn"]/state_data["Players"]

        # Création de la carte Folium
        m = folium.Map(location=[47, 2], zoom_start=2)

        # Sélection des 10 premiers du top ratio
        top = state_data.head(self.classement)

        # Formatage des données dans une chaîne de texte
        top_text = ""  # Initialisation de top_text
        top = state_data.sort_values(by="Ratio", ascending=False).head(self.classement)
        for index, row in top.iterrows():
            words = row['Country'].split()  # Diviser la chaîne en mots
            half_length = len(words) // 2  # Calculer la moitié du nombre de mots
            first_half = " ".join(words[:half_length])  # Joindre la première moitié des mots
            top_text += f"{first_half}: {row['Ratio']:.2f}$\n"          
        
        # Ajout de la choroplèthe à la carte
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=top,
            columns=["Country", "Ratio"],
            key_on="feature.properties.name",
            nan_fill_color="White",
            fill_color="Purples",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Ratio argent gagné / joueur",
        ).add_to(m)

        folium.LayerControl().add_to(m)
        
        # Trie des données selon le ratio
        state_data.sort_values(by="Ratio", ascending=False, inplace=True)  
            
        print(top_text)
            
        return  m
    
# Instanciation d'un objet Donnees avec des valeurs arbitraires
donnees_esports = Esport(2011,10)

# Appel de la méthode ratio() sur l'instance de Donnees
carte = donnees_esports.ratio()

carte
