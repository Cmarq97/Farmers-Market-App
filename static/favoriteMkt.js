$(document).ready(function() {

    document.getElementById("favorite").onclick = function (event) {
        alert("Favorite Added");
        event.preventDefault();
        market_id = $('#market_id').val();
        $.post('/markets/' + market_id);
    }
})
