$(document).ready(function() {

    document.getElementById("favorite").onclick = function (event) {
        alert("Favorite Added");
        event.preventDefault();
        vendor_id = $('#vendor_id').val();
        $.post('/vendors/' + vendor_id);
    }
})