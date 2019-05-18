import googlemaps

gmaps = googlemaps.Client('AIzaSyBDU_vUpEHdaYOwvFi_QdnfbFQYIfBf0sk')

origen = 'farmacia central, Tandil, Buenos Aires'

#con geocode me quedo con place_id
geocode_result = gmaps.geocode(origen)
geocode_result0 = geocode_result[0]
placeId = geocode_result0['place_id']

#con place(place_id) obtengo las fotos del lugar
place = gmaps.place(placeId)
pl = place['result']
if pl.has_key('photos'):
    for i in pl['photos']:
        print i
    print "cantidad de fotos del lugar: " ,len(pl['photos'])
else:
    print "lugar sin fotos"
#BUSCAR FOTO
# https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAqNOFbavAsaSaw0AVOpmG0Iq7v806qjKsQmO2I7NswblNXmLVSdx77KjGYQw3k7vjqnTSGEtop10YRGmbt0ZgIvm6jVltfKbepUGQ11H3JFg4DQTUIYjfxGvWD-Kphu6aEhDT93Y79wtxcVuWDsoWwzVzGhQiCP0IJtIOojBruL1lBqYvTaGuOw&key=AIzaSyBDU_vUpEHdaYOwvFi_QdnfbFQYIfBf0sk



#tambien podriamos buscar los lugares cercanos (radio = 2 o 3 cuadras), de todos los rubros de google maps
#y si la cantidad de lugares > X entonces es muy popular... pero son muchos for y no se como va a quedar.



"""
geoco = gmaps.geocode(origen)
geoco0 = geoco[0]
geoco0id =  geoco0['place_id']

place = gmaps.place(geoco0id)
#print place

place_photo = gmaps.places_photo(geoco0id, 2000, 2000)
print place_photo
"""