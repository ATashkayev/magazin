$(document).ready(function(){
    var form = $('#form_buy_product');
    //console.log(form);


     function basket_update(prod, numprod, price, is_delete ){
      var data = {};

    data.product_id = prod;
    data.nmb = numprod;
    data.price = price;
    data.is_delete = is_delete;
    console.log(data);
    var csrf_token = $('#id_csrf_token [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;
    console.log(csrf_token);
    var url = "/basket/";//form.attr("action");


    $.ajax({

        url: url,

        type: 'POST',

        data: data,

        cache: true,

        success: function (data) {
            console.log("OK");
	        console.log(data.products_total_nmb);

            if (data.products_total_nmb || data.products_total_nmb==0) {
                $('#basket_total_nmb').text("  ("+data.products_total_nmb+")");

                console.log(data.products);
                $('#basket-item ul').html("");

                $.each(data.products, function(k, v){

                $('#basket-item ul').append('<li>'+ v.name+', ' + v.nmb + ' шт. цена ' + v.price_per_item + 'грн. ' +
	                ' на ' + v.nmb*v.price_per_item+ ' грн.   '+
                '<a class="delete-item" href="" data-product_id="'+v.product_id+'"><span  class="glyphicon glyphicon-minus-sign" aria-hidden="true"></span></a></li>');

                    });

                 $('#basket-item ul').append('<ul><a href="/checkout/"> Оформить заказ </a></ul>');


            };



    }
    });

     }

    form.on('submit', function(elem){
       //
        var numprod = $('#number_prod').val();
        var butt    = $('#submit_btn');
        var prod    = butt.attr("product_id");
        var price    = butt.attr("product_price");
        var product_name    = butt.attr("product_name");
        console.log(price);
        console.log(prod);

        basket_update(prod, numprod, price, is_delete = false);

     elem.preventDefault();
    });



  $('#basket-conteiner').on('click', function(e){
   // e.preventDefault();
   // console.log(e);
    $('#basket-item').show();
  });

   $('#basket-conteiner').mouseover(function(){
    $('#basket-item').show();
  });

  $('#basket-conteiner').mouseout(function(){
    $('#basket-item').hide();
  });

  $(document).on('click', '.delete-item', function(elem){
    elem.preventDefault();
    prod = $(this).attr("data-product_id");
    basket_update(prod, 0, 0, is_delete = true);
    $(this).closest('li').remove();
  });

    function calculatingBasket(){
        var total_order_amount =0;
        $('.total-product-in-basket-amount').each(function(){
                total_order_amount += Number(parseFloat($(this).text()).toFixed(2));
                })
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };

    $(document).on('change','.product-in-basket-nmb',function(){
        var current_nmb   = $(this).val();
        var current_item  = $(this).closest('tr');
        var current_price = Number(parseFloat(current_item.find('.product-price').text()).toFixed(2));
        var total_amount  = (current_nmb*current_price);
        total_amount  = Number(total_amount.toFixed(2));
        current_item.find('.total-product-in-basket-amount').text(total_amount.toFixed(2));

        calculatingBasket();
    });

calculatingBasket();
});