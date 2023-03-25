import folium
# import pandas as pd

m = folium.Map(location=[50.04908088464327, 21.981612615229974], title='Stamen Terrain', zoom_start=6, width=950, height=650)

# to mozna for z jakiegos arraya zamiast pojedynczo
m.add_child(folium.Marker(location=[50.04908088464327, 21.981612615229974], popup="nasz marker: Rzeszów", icon=folium.Icon("red")))
m.add_child(folium.Marker(location=[49.949890921270715, 22.058874020398942], popup="nasz marker: Kielnarowa ", icon=folium.Icon("green")))
m.add_child(folium.Marker(location=[50.08951265233697, 21.520494332301062], popup="nasz marker: Paszczyna", icon=folium.Icon("blue")))

with open("Volcanoes.txt", mode='r') as v:
        for volcano in v.readlines()[1:]:
            params = volcano.strip().split(',')
            folium.map.Marker([float(params[-2]), float(params[-1])], popup=params[3], icon=folium.Icon("orange")).add_to(m)
m.save('map.html')


# pandas
# data = pd.read_cs('Volcanoes.txt')