



function saveFavorite(marker) {
    data = {obj: marker};
    console.log(data);
    console.log(JSON.stringify(data));
    $.post("/save_favorite/", JSON.stringify(data), function(response){
    }, 'json');
}

