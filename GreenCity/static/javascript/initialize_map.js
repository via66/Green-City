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
    var icon;
    var markers;
    for (var i = 0; i < data.length; i++)
    {
        var data_point = data[i];
        icon = markerIcons[data_point.ftype];
        var coord = new google.maps.LatLng(data_point.lat, data_point.long);
        var marker = new google.maps.Marker({
            position: coord,
            map: map,
            icon: icon
        });
        marker.description = data_point.name;
        google.maps.event.addListener(marker, 'click', function () {
            var infowindow = new google.maps.InfoWindow();
            infowindow.setContent(this.description);
            infowindow.open(map, this);
        });
    };
}
