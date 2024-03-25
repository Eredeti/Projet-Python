def marqueur(coordonnees):
#////////////////////////////////////////////////
    somme_x, somme_y = 0, 0
    n = len(coordonnees)
    for x, y in coordonnees:
        somme_x += x
        somme_y += y

    centre = [somme_x / n, somme_y / n]
    m = folium.Map(centre, zoom_start = 15)
    folium.Marker( 
        location = centre,
        tooltip = "ICI",
        popup = "je ne sais pas",
        icon = folium.Icon(icon = "check", color = "red"),
    ).add_to(m)

    return m
