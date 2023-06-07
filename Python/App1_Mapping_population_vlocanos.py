from os import name
import folium, pandas

#import volcanos text file
data = pandas.read_csv(r'C:\Users\bisha\Desktop\Bob\Python\App1Files\Volcanoes.txt')
print(data.columns) #print all column names

#converting latitude values to a list from dataframe
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location = [38.58, -99.09],zoom_start=5, tiles='Stamen Terrain') #tiles='Stamen Terrain'
#zoom_starts = 6 - this can be used to zoom out in the map

#featuregroup
fgv = folium.FeatureGroup(name = 'Volcanos')

#now iterate through lat and ln using zip func
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location = [lt, ln], popup=str(int(el))+' m', icon=folium.Icon(color='beige')))

fgp = folium.FeatureGroup(name = 'Population')
#geo json - adding population
fgp.add_child(folium.GeoJson(data =open(r'C:\Users\bisha\Desktop\Bob\Python\App1Files\world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <- x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save(r'C:\Users\bisha\Desktop\Bob\Python\App1Files\maptest.html')





#----------------------basic steps------------------------------
#map = folium.Map(location = [18.588487, 73.683800]) #tiles='Stamen Terrain' #This was co-ordinate of pune flat
#map.add_child(folium.Marker(location = [18.588487, 73.683800], popup='I am marker'))
#map.save(r'C:\Users\bisha\Desktop\Bob\Python\App1Files\maptest.html')
