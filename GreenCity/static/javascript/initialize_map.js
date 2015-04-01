/**
 * Created by Walter on 3/8/2015.
 */
var markerSize = new google.maps.Size(21, 34);
var markerOrigin = new google.maps.Point(0, 0);
var markerAnchor = new google.maps.Point(10, 34);
var iconURL = "http://chart.apis.google.com/chart?chst=d_map_xpin_letter&chld=";
var markerIcons = {};
markerIcons['Park'] = "%E2%80%A2|a4de94";
markerIcons['GreenCityProject'] = "%E2%80%A2|f75a70";
markerIcons['BikeRack'] = "99dbf6";
markerIcons['ElectricVehicleChargingStation'] = "%E2%80%A2|f3e37b";
markerIcons['CommunityGarden'] = "%E2%80%A2|dc99e2";
markerIcons['CommunityFoodMarket'] = "%E2%80%A2|f5a864";

function plot_markers(map, data) {
    for (var i = 0; i < data.length; i++)
    {
        if (data[i].favourite == 1){
            customIconURL = iconURL + "pin_star|" + markerIcons[data[i].ftype] + "||f5a864"
        } else {
            customIconURL = iconURL + "pin|" + markerIcons[data[i].ftype]
        }
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(data[i].latitude,data[i].longitude),
            map: map,
            icon: new google.maps.MarkerImage(customIconURL, markerSize, markerOrigin, markerAnchor)
        });
        marker.fname = data[i].fname;
        marker.description = data[i].description;
        marker.ftype = data[i].ftype;
        google.maps.event.addListener(marker, 'click', function () {
            var infowindow = new google.maps.InfoWindow();
            infowindow.setContent(this.description + '<br/> <button class="btn btn-sm content-btn" onclick="saveFavorite(\'' + this.fname + '\')">Favorite!</button>' + '<button class="btn btn-sm content-btn" onclick="removeFavorite(\'' + this.fname + '\')">Unfavorite!</button>');
            infowindow.open(map, this);
        });
        mapMarkers.push(marker);
    }
    markerCluster = new MarkerClusterer(map, mapMarkers);
}


function clear_markers() {
  for (var i = 0; i < mapMarkers.length; i++) {
    mapMarkers[i].setMap(null);
  }
  mapMarkers = [];
  markerCluster.clearMarkers();
}

function plot_heatmap(map, data){
    var list_data = $.map(data, function (elem, indx) {
        return new google.maps.LatLng(elem.latitude,elem.longitude);
    });
    var heatmap = new google.maps.visualization.HeatmapLayer({
        data: list_data,
        dissipating: false,
        radius: 0.002,
        maxIntensity: 1
     });
    heatmap.setMap(map);
    return heatmap;
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}
