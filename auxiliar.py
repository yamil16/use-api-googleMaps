latitud="-37.328013,"
longitud="-59.137375"
archivoDatos = open('datosMapaAuxiliar.txt','w')
mapa3="""<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map_canvas { height: 100% }
    </style>
  <script type="text/javascript" src="http://maps.googleapis.com/maps/api/js?key=AIzaSyBDU_vUpEHdaYOwvFi_QdnfbFQYIfBf0sk&libraries=places&sensor=true"></script>
    <script type="text/javascript">
    var map;
        var service;
        var infowindow;
     
     
        function initialize() {
            var pyrmont = new google.maps.LatLng(-37.328013,-59.137375);
     
            map = new google.maps.Map(document.getElementById('map'), {
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                center: pyrmont,
                zoom: 6
            });
     
            var request = {
                location: pyrmont,
                radius: '5000',
                query: 'verduleria'
            };
     
            infowindow = new google.maps.InfoWindow();
            var service = new google.maps.places.PlacesService(map);
            service.textSearch(request, function(results, status) {
                if (status == google.maps.places.PlacesServiceStatus.OK) {
                    for (var i = 0; i < results.length; i++) {           
                        createMarker(results[i]);

                    }
                }
            });
        }
     
        function createMarker(placeMarker) {
            var marker = new google.maps.Marker({
                map: map,
                position: placeMarker.geometry.location
            });
     
            google.maps.event.addListener(marker, 'click', function() {
                infowindow.setContent(placeMarker.name);
                infowindow.open(map, this);
            });
        }
    </script>
  </head>
  <body onload="initialize()">
    <div id="map" style="width:650px; height:650px"></div>
  </body>
</html>"""
#archivoDatos.writelines(results)
archivoDatos.close()
archivo = open('mapaAuxiliar.html','w')
archivo.write(mapa3)
archivo.close()
