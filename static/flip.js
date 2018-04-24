/* card flip */
window.onload = function(){
$(".flip").hover(function(){
  $(this).find(".card").toggleClass("flipped");
  return false;
});
}
