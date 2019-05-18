import googlemaps
from datetime import datetime

gmaps = googlemaps.Client('AIzaSyDrL4F68m0CKyyK9_OJV14e60FRAIULRrQ')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
places_radar_result = gmaps.places_radar(location=(40.714224, -73.961452), radius=1000, keyword='pharmacy')
#print "hola"
#print places_radar_result
id_list = []

for i in places_radar_result['results']:
    id_list.append(i['place_id'])

place = gmaps.place(id_list[0])
print id_list #todos los id de los lugares
print place #toda la informacion del lugar esee

#json_test = {'nombre': '', 'edad': 0, 'hijos': [], 'padre': {}}

#json_test['nombre'] = 'tomas'
#json_test['edad'] = 45
#json_test['hijos'].append('Juan')
#json_test['hijos'].append('Maria')

#print json_test['nombre']
#print json_test['edad']
#print json_test['hijos']
#print type(json_test)

lista=[]
json_test = {'nombre': '', 'id': 0, 'latitud': 0, 'longitud': 0,'distancia':0}
for pos in places_radar_result['results']:
       # json_test['nombre']=pos['name']
        json_test['id'] = pos['place_id']
        json_test['latitud'] = pos['geometry']['location']['lat']
        json_test['longitud'] =pos['geometry']['location']['lng']
        lista.append(json_test)

print "hola json test imprimo:"
print lista