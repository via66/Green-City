/**
 * Created by Walter on 3/8/2015.
 */
function plot_markers(map, data) {
    var markerSize = new google.maps.Size(21, 34);
    var markerOrigin = new google.maps.Point(0, 0);
    var markerAnchor = new google.maps.Point(10, 34);
    var customIconURL = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|";
    var markerIcons = {};
    markerIcons['Park'] = new google.maps.MarkerImage(customIconURL + "a4de94", markerSize, markerOrigin, markerAnchor);
    markerIcons['GreenCityProject'] = new google.maps.MarkerImage(customIconURL + "f75a70", markerSize, markerOrigin, markerAnchor);
    markerIcons['BikeRack'] = new google.maps.MarkerImage(customIconURL + "99dbf6", markerSize, markerOrigin, markerAnchor);
    markerIcons['ElectricVehicleChargingStation'] = new google.maps.MarkerImage(customIconURL + "f3e37b", markerSize, markerOrigin, markerAnchor);
    markerIcons['CommunityGarden'] = new google.maps.MarkerImage(customIconURL + "dc99e2", markerSize, markerOrigin, markerAnchor);
    markerIcons['CommunityFoodMarket'] = new google.maps.MarkerImage(customIconURL + "f5a864", markerSize, markerOrigin, markerAnchor);
    for (var i = 0; i < data.length; i++)
    {
        var marker = new google.maps.Marker({
            position: data[i].pos,
            map: map,
            icon: markerIcons[data[i].ftype]
        });
        marker.description = data[i].name;
        google.maps.event.addListener(marker, 'click', function () {
            var infowindow = new google.maps.InfoWindow();
            infowindow.setContent(this.description);
            infowindow.open(map, this);
        });
    }
}

function plot_heatmap(map, data){
    var list_data = $.map(data, function (elem, indx) {
        return elem.pos;
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