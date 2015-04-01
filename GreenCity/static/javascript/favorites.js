



function saveFavorite(marker) {
    data = {obj: marker};
    console.log(data);
    console.log(JSON.stringify(data));
    $.post("/save_favorite/", JSON.stringify(data), function(response){
            console.log('hello');
            set_favourite(marker);
    }, 'json').done(function(){console.log('this worked');}).fail(function(){console.log('fail');});
}

function removeFavorite(marker) {
    data = {obj: marker};
    console.log(data);
    console.log(JSON.stringify(data));
    $.post("/remove_favorite/", JSON.stringify(data), function(response){
        console.log('hello');
        unset_favourite(marker);
    }, 'json').done(function(){console.log('this worked');}).fail(function(){console.log('fail');});
}


function set_favourite(marker_name){
    for (var i=0 ; i < mapMarkers.length; i++){
        console.log(marker_name);
        if (mapMarkers[i].fname == marker_name){
            console.log(mapMarkers[i].fname);
            customIconURL = iconURL + "pin_star|" + markerIcons[mapMarkers[i].ftype] + "||f5a864";
            mapMarkers[i].setIcon(new google.maps.MarkerImage(customIconURL, markerSize, markerOrigin, markerAnchor));
        }
    }
}

function unset_favourite(marker_name){
    console.log(marker_name);
    for (var i=0 ; i < mapMarkers.length; i++){
        if (mapMarkers[i].fname == marker_name){
            console.log(mapMarkers[i].fname);
            customIconURL = iconURL + "pin|" + markerIcons[mapMarkers[i].ftype];
            mapMarkers[i].setIcon(new google.maps.MarkerImage(customIconURL, markerSize, markerOrigin, markerAnchor));
        }
    }
}