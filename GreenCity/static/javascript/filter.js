$('button#submitButton').click( function() {
    $.ajax({
        url: '/filter/',
        type: 'POST',
        dataType: 'json',
        data: $('#filterForm').serialize(),
        success: function(data) {
        console.log(data[0])
		console.log("hello");
		var map;
		console.log("inside initalize");
		var mapOptions = {
			zoom: 12,
			center: new google.maps.LatLng(49.2827, -123.1207)
		};
		map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
		var features = [];
		for(i=0; i <= data.length-1; i++){
			console.log(i);
			console.log(data[i]);
			console.log(data[i].fields.name);
			features.push( { name: data[i].fields.name,
					 pos: new google.maps.LatLng(data[i].fields.latitude,data[i].fields.longitude)
			});
		}
		plot_markers(map, features);
		console.log(features);
                alert("Success!");
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