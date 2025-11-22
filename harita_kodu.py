#modüller: 
import folium as fl 
import branca.colormap as cm

#colorMap settings
colors = ['green','green','red','red','yellow','yellow','orange','orange','blue','blue','blue']
vmin = 0
vmax = 10

#map
CustomMap = fl.Map(location=[40,45],
       zoom_start=4,
       tiles='CartoDB DarkMatter'
      )

#locations
locationMatrix = [
    [30.0444, 31.2357],   # Kahire
    [36.8065, 10.1815],   # Tunus (doğum ve dönüş dönemi)
    [34.0331, -5.0000],   # Fas (Fes bölgesi)
    [36.7509, 5.0567],    # Becâye (Béjaïa)
    [37.1773, -3.5986],   # Gırnata (Granada)
    [36.8065, 10.1815],   # Tunus (geri dönüş tekrar)
    [36.7509, 5.0567],    # Becâye (valilik dönemi)
    [34.8504, 5.7280],    # Biskra
    [36.7069, 4.0450],    # Kabiliye (Tizi Ouzou civarı)
    [31.2001, 29.9187],   # İskenderiye
    [33.5138, 36.2765]    # Şam
]

locationStrings = [
    'Kahire',
    'Tunus',
    'Fas',
    'Becaye',
    'Gırnata',
    'Tunus',
    'Becaye',
    'Biskra',
    'Kabiliye',
    'g',
    'Şam'
]

#drawCircleMarkers
for latlon,color,locs in zip(locationMatrix,colors,locationStrings):
    circleMarker = fl.CircleMarker(location=latlon,
                                   fill=True,
                                   fill_opacity=0.5,
                                   color=color,
                                   radius=15,
                                   popup=locs

                                  ).add_to(CustomMap)
    

LinearColorMap = cm.LinearColormap(colors=colors,
                                   vmin=0,
                                   vmax=10,
                                   caption='0-10 Arası Renk Skalası',
                                   text_color='white'
                                   ).add_to(CustomMap)

CustomMap.save('circle_map.html')
