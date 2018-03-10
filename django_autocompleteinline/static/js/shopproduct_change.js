(function($){
  $(function(){
    var inline = 'shopproduct_set';

    function select_watcher() {
      $(`.dynamic-${inline}`).each(function(index) {
        var select = $(`#id_${inline}-${index}-product`);
        var price_input = $(`#id_${inline}-${index}-price`);
        select.bind('change', function() {
          var product_name = select.find('option:selected').text();
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
      select_watcher();
      // as long as select_watcher does not include return false;
      // it shouldn't interfere with the existing functionality of that button.
      $('.add-row a').click(select_watcher);
    });
  });
})(django.jQuery);
