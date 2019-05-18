latitud="-37.328013,"
longitud="-59.137375"
mapa3="""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Search for up to 200 places with Radar Search</title>
    <style>
       html, body, #map_canvas {
          height: 500px;
          width: 500px;
          margin: 0px;
          padding: 0px
      }
    </style>
   
  </head>
  <body>
   <script>
        function initialize() {
        var resultsMap = new google.maps.Map(
            document.getElementById("map_canvas"), {
                center: new google.maps.LatLng(37.4419, -122.1419),
                zoom: 13,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });
        ////function,google.maps.geometry.spherical.computeDistanceBetween (x,y) is what i am using to do that ,so how to insert the request.location value as x
        var x=new google.maps.LatLng(52.395715,4.888916);
            var requestLocation = new google.maps.Marker({
                position: x,
                map: resultsMap,
                title: "request position",
                icon: "http://maps.google.com/mapfiles/ms/micons/blue.png"
            });
         var request={
                        location: x,
                        radius: '500',
                        query: 'restaurant'
                            };
        var  service=new google.maps.places.PlacesService(resultsMap);
                        service.textSearch(request, callback);
        function callback(results,status) {
                if (status == google.maps.places.PlacesServiceStatus.OK) {
                    var bounds = new google.maps.LatLngBounds();
                    for (var i = 0; i < results.length; i++) {
                        var y = results[i].geometry.location;
                           document.getElementById("distance").innerHTML += "["+i+"]  name:"+results[i].name+", distance="+(google.maps.geometry.spherical.computeDistanceBetween (x,y)/1000).toFixed(2)+" km<br>";
                        console.log(y);
                        var marker = new google.maps.Marker({
                            position: results[i].geometry.location,
                            map: resultsMap,
                            title: results[i].name
                        });
                        bounds.extend(marker.getPosition());
                    }
                    resultsMap.fitBounds(bounds);
                }

            }
        }
        google.maps.event.addDomListener(window, "load", initialize);


    </script>
      <div id="distance"></div>
      <div id="map_canvas" style="width:750px; height:450px; border: 2px solid #3872ac;"></div>

   </body>
</html>"""

archivo = open('mapaLugaresv4.html','w')
archivo.write(mapa3)
archivo.close()