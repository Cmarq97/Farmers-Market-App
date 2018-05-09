function initIndivMktMap() {
    let myLatLng = {lat: 37, lng: -121};

    // Create a map object and specify the DOM element for display.
    let map = new google.maps.Map(document.getElementById('indiv-market-map'), {
        center: myLatLng,
        scrollwheel: false,
        zoom: 8,
        zoomControl: true,
        panControl: false,
        streetViewControl: false,
        styles: MAPSTYLES
    });

    if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(function (position) {
         initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
         map.setCenter(initialLocation);
         var userMarker = new google.maps.Marker({
            position: initialLocation,
            map: map,
            icon: '/static/img/Icons/house.png'});
     });
    }
    market_id = $('#market_id').val();
    // Retrieving the information with AJAX
    $.get('/markets/' + market_id + '.json', function (market_info){

        let market_location = new google.maps.Geocoder();
        let address = market_info.address;

        market_location.geocode({'address': address},
          function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
              marker = new google.maps.Marker({
                title: market_info.name,
                map: map,
                icon: '/static/img/Icons/market.png',
                position: results[0].geometry.location
              });
            } else {
              // alert('Geocode was not successful for the following reason: ' + status);

            }
        })
    })
}
//waits for page to fully load before executing JavaScript
google.maps.event.addDomListener(window, 'load', initIndivMktMap);
google.maps.event.addDomListener(window, 'page:load', initIndivMktMap);
// document.addEventListener("turbolinks:load", initIndivMktMap);