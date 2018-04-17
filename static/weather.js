function initWeather(){
    market_id = $('#market_id').val();
        // Retrieving the information with AJAX
    $.get('/markets/' + market_id + '/weather', function (result){$('#weather-div').html(result)})
}

google.maps.event.addDomListener(window, 'load', initWeather);