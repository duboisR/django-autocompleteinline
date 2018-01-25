(function($){
  $(function(){
    var inline = 'shopproduct_set';

    function autocomplete_watcher() {
      $(`.dynamic-${inline}`).each(function(index) {
        var span = $(`#select2-id_${inline}-${index}-product-container`);
        var price_input = $(`#id_${inline}-${index}-price`);
        span.bind('DOMNodeInserted', function() {
          var product_name = span[0].firstChild.data;
          $.ajax({
            'type'     : 'GET',
            'url'      : `/api/product_price/?product_name=${product_name}`,
            'dataType' : 'json',
            'cache'    : false,
            'success'  : function(json) {
              price_input[0].value = json['price'];
            }
          });
        });
      });
    }

    $(document).ready(function() {
      autocomplete_watcher();
      // as long as autocomplete_watcher does not include return false;
      // it shouldn't interfere with the existing functionality of that button.
      $('.add-row a').click(autocomplete_watcher);
    });
  });
})(django.jQuery);
