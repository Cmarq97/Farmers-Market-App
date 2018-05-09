$(document).ready(function(){

   $('input[name="search_by"]').on('change', function() {
      let search_by = $('input[name=search_by]:checked').val();

      let search_values;
      $.getJSON('/autocomplete/' + search_by, function(result) {
         search_values = result;
      $("#autocomplete").autocomplete({
         minLength:2,   
         delay:100,   
         source: search_values
      });
      });
   });
});