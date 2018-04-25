/* card flip */
window.onload = function(){
$(".flip").hover(function(){
  $(this).find(".card").toggleClass("flipped");
  return false;
});
$(".flip").on('click', function(evt){
    window.open('/vendors/' + evt.target.dataset.vendorid);
});
}
