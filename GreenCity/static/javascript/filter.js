$('button#submitButton').click( function() {
    $.ajax({
        url: '/filter/',
        type: 'POST',
        dataType: 'json',
        data: $('#filterForm').serialize(),
        success: function(data) {
            clear_markers();     
            console.log(data[0])

    		var features = [];
    		for(i=0; i <= data.length-1; i++){
    			console.log(i);
    			console.log(data[i]);
    			console.log(data[i].fields.name);
    			features.push( { ftype: data[i].fields.ftype, name: data[i].fields.name,
    					 pos: new google.maps.LatLng(data[i].fields.latitude,data[i].fields.longitude)
    			});
    		}
    		plot_markers(map, features);
    		console.log(features);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });
});

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