
var coord = [46.71377, 11.65998];
var mkr = L.marker(coord);
var mymap = L.map('italianmap').setView([46.7139, 11.659], 14);
var popup = L.popup();

function updatePosition() {
    "use strict";
    coord[0] = (((Math.random()) / 50) + 46.7039);
    coord[1] = (((Math.random()) / 50) + 11.649);
    mkr._latlng = coord;
    mkr.update();
}
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: 'mapbox.streets'
}).addTo(mymap);
var tim = setInterval(updatePosition, 1000);
mkr.addTo(mymap);