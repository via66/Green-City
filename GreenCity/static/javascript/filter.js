function filter_data() {
    $.ajax({
        url: '/filter/',
        type: 'POST',
        dataType: 'json',
        data: $('#filterForm').serialize(),
        success: function(features) {
            heatmap.setMap(null);
            clear_markers();
    		plot_markers(map, features);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });
}

$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});


$( '#filterForm' ).ready(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(fillLocation);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
});

function fillLocation(position) {
    $( '#usr_lat' ).val(position.coords.latitude);
    $( '#usr_long' ).val(position.coords.longitude); 
}

$('#feature_checker').change(function(){
    if($(this).prop('checked')){
        $('input[type="checkbox"]').each(function(){
            $(this).prop('checked', true);
        });
    }else{
        $('input[type="checkbox"]').each(function(){
            $(this).prop('checked', false);
        });
    }
});

$('#logout').click(function(e){
	data = {zoom_level:map.getZoom(), lat_long:map.getCenter()};
	console.log(JSON.stringify(data));
	$.post("/save/", JSON.stringify(data), function(response){
	}, 'json');
});
