function initMap() {
    let myLatLng = {lat: 37, lng: -121};

    // Create a map object and specify the DOM element for display.
    let map = new google.maps.Map(document.getElementById('market-map'), {
        center: myLatLng,
        scrollwheel: false,
        zoom: 5,
        zoomControl: true,
        panControl: false,
        streetViewControl: false,
    });
    market_id = $('#market_id').val();
    // Retrieving the information with AJAX
    $.get('/market/' + market_id + '.json', function (market_info){

        let market_location = new google.maps.Geocoder();
        let address = market_info.address;

        market_location.geocode({'address': address},
          function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
              marker = new google.maps.Marker({
                title: market_info.name,
                map: map,
                position: results[0].geometry.location
              });
            } else {
              alert('Geocode was not successful for the following reason: ' + status);

            }
        })
    })
}
//waits for page to fully load before executing JavaScript
google.maps.event.addDomListener(window, 'load', initMap);