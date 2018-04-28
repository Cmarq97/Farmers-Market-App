function initMap() {
    // Specify where the map is centered
    let myLatLng = {lat: 37.3, lng: -122};

    // Create a map object and specify the DOM element for display.
    let map = new google.maps.Map(document.getElementById('market-map'), {
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
            title: "Your Current Location",
            icon: '/static/img/Icons/house.png'});
     });
    }

    // Allows us to create one info window and replace contents for each market marker
    let infoWindow = new google.maps.InfoWindow({
        width: 150
    });
    vendor_id = $('#vendor_id').val();
    // Retrieving the information with AJAX
    $.get('/vendors/' + vendor_id + '/json', function (markets) {
      // JSON looks like:
    // market_data = {
    // "marketId": market.market_id,
    // "day": market.market_day,
    // "startTime": market.market_start.strftime('%I:%M %p'),
    // "endTime": market.market_end.strftime('%I:%M %p'),
    // "address": market.market_address
    // }

      let market, marker, html;

      for (let key in markets) {
            market = markets[key];
            addMarketByAddress(market);
          }
      });

      function addMarketByAddress(market) {
        let market_location = new google.maps.Geocoder();
        let address = market.address;
        market_location.geocode({'address': address},
          function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
              marker = new google.maps.Marker({
                title: market.market_name,
                icon: market.icon,
                map: map,
                position: results[0].geometry.location
              });

              html = (
              '<div class="window-content">' +
                    '<p><b>Market Name: </b>' + market.name + '</p>' +
                    '<p><b>Day: </b>' + market.day + '</p>' +
                    '<p><b>Time: </b>' + market.startTime + '-' + market.endTime + '</p>' +
                    '<p><b>Address: </b>' + market.address + '</p>' +
              '</div>');
              
              bindInfoWindow(marker, map, infoWindow, html);
            } else {
              // alert('Geocode was not successful for the following reason: ' + status);
            }
        });
            
    function bindInfoWindow(marker, map, infoWindow, html) {
        google.maps.event.addListener(marker, 'click', function () {
            infoWindow.close();
            infoWindow.setContent(html);
            infoWindow.open(map, marker);
        });
    }
}
}

//waits for page to fully load before executing JavaScript
google.maps.event.addDomListener(window, 'load', initMap);