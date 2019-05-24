import folium
import folium.plugins as plugins
import csv
from datetime import datetime

m = folium.Map([39.01, -94.56], tiles='stamentoner', zoom_start=4)

# On instancie 6 listes dans la variable data qui vont correspondre aux annees 2011-2016
data = [ [],[],[], [], [], [] ]
time = []

cities = [
  [38.9072, -77.0369], # Washington
  [37.7749, -122.4194] # San fransico
]

cities_line = folium.PolyLine(
  cities,
  weight=8,
  color='red'
).add_to(m)

attr = {'fill': '#007DEF', 'font-weight': 'bold', 'font-size': '24'}
plugins.PolyLineTextPath(
  cities_line,
  '( ',
  repeat=True,
  offset=7,
  attributes=attr
).add_to(m)

with open('data_diabetes_bfrss_USA.csv') as csvfile:
  # On ignore la premiere ligne contenant les en-tetes
  next(csvfile)
  
  # On parse le contenu du fichier csv
  rows = csv.reader(csvfile, delimiter=',')

  for row in rows:
    lat = float(row[2].split(',')[0].replace('(', ''))
    lng = float(row[2].split(',')[1].replace(')', '').strip())
    weight = float(row[1])/100 # Diviser par 100 car le poids est compris entre 0 et 1
    year_num = int(row[0].replace(' Average', ''))

    # On positionne le point au bon index data correspondant a l'annee
    i = year_num - 2011
    point = [lat, lng, weight]
    data[i].append(point)

# Creer la table de temps (variable time) (2011-2016)
for j in range(2011,2017):
  d = datetime(year=j, month=1, day=1)
  time.append(d.strftime('%Y-%m-%d'))


hm = plugins.HeatMapWithTime(
    data,
    index=time,
    auto_play=True,
    radius=50,
    min_opacity=0.4
  )

hm.add_to(m)
m.save('map.html')

print('/app/map.html')
