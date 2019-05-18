#dada la direccion, geocode la transforma a latitud y longitud; para que se pueda hacer la busqueda de place_radar que muestra los lugares cercanos, del rubro cargado, y esa lista se pasa por distance matrix, que muestra la distancia en metros, respecto al origen
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client('AIzaSyBDU_vUpEHdaYOwvFi_QdnfbFQYIfBf0sk')
origen = 'San Lorenzo 283, Tandil, Buenos Aires'
clave = 'pharmacy'

#geocode para obtener la longitud y latitud
geocode_result = gmaps.geocode(origen)
geocode_result0 = geocode_result[0]
geocode_result0g = geocode_result0['geometry']
geocode_result0gl = geocode_result0g['location']
print geocode_result0gl #latitud y longitud de la direccion de origen
latitud = geocode_result0gl['lat']
longitud = geocode_result0gl['lng']

#places_radar para buscar la competencia del rubro "clave", en un radio de 1 km de la locacion elegida
now = datetime.now()
places_radar_result = gmaps.places_radar(location=(latitud, longitud), radius=1000, keyword=clave)
id_list = []
for i in places_radar_result['results']:
    id_list.append(i['place_id'])

#por cada competencia, place me da los datos (nombre, rating, place_id...)
for j in range(len(id_list)):
    place = gmaps.place(id_list[j])
    pl = place['result']
    list_place_name = pl['name']
    if pl.has_key('rating'):
        print list_place_name, ". Rating: ", pl['rating']
    else:
        print list_place_name, ". Sin rating"

    list_place_id = pl['place_id']
    gplace = gmaps.place(list_place_id)
    gplaceRes = gplace['result']
    gplaceResAdd = gplaceRes['address_components']
    gplaceResAdd0 = gplaceResAdd[0]
    gplaceResAdd1 = gplaceResAdd[1]
    gplaceResAdd2 = gplaceResAdd[2]
    gplaceResAdd4 = gplaceResAdd[4]

    placeStreet = gplaceResAdd1['long_name']
    placeNumber = gplaceResAdd0['short_name']
    placeCity = gplaceResAdd2['long_name']
    placeProvince = gplaceResAdd4['long_name']

    list_place_name_complete = placeStreet + " " + str(placeNumber) + ", " + placeCity + ", " + placeProvince
    print list_place_name_complete


    distance_matrix = gmaps.distance_matrix(origen, list_place_name_complete, mode = 'walking')
    distance_matrixr = distance_matrix['rows']
    distance_matrixr0 = distance_matrixr[0]
    distance_matrixr0e = distance_matrixr0['elements']
    distance_matrixr0e0 = distance_matrixr0e[0]
    if distance_matrixr0e0 ['status'] != 'NOT_FOUND':
        distance_matrixr0e0d = distance_matrixr0e0['distance']
        resul = distance_matrixr0e0d['value']
        print "distancia desde ", origen, ": ", resul, "metros"
    else:
        print "lugar no encontrado en Google Maps."

print "\nCantidad de lugares de la competencia en las cercanias de la zona: " ,len(id_list)
if len(id_list) > 10:
    print "Hay mucha competencia en el lugar (mas de 10)"
else:
    if len(id_list) > 5:
        print "Hay competencia moderada en el lugar (mas de 5 y menos de 10)"
    else:
        print "Hay poca competencia en el lugar (menos de 5)"
