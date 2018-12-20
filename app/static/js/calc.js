jQuery(document).ready(function () {
 
    function update_prices(){
        var mult_roznica = $('#modifroznica').val();
        var mult_opt = $('#modifopt').val();
        var price_roznica; 
        var price_opt;
        if (mult_roznica != 0 || mult_roznica != null){
            if(mult_roznica > 0){
                if ($('#minprice').val()!= "")
                {
                    if ($('#minprice').val() > (Math.ceil($('#oneprice').val()*(mult_roznica/100+1)/50)*50))
                    {
                        $('#rozniceprice').val($('#minprice').val());
                    }
                    else
                    {
                        $('#rozniceprice').val(Math.ceil($('#oneprice').val()*(mult_roznica/100+1)/50)*50);
                    };
                }
                else
                {
                    $('#rozniceprice').val(Math.ceil($('#oneprice').val()*(mult_roznica/100+1)/50)*50);
                };                
            };
            if (mult_opt != 0){
                
                if(mult_opt > 0){
                    $('#optprice').val(Math.ceil($('#oneprice').val()*(mult_opt/100+1)/10)*10);
                }else{
                    $('#optprice').val(Math.ceil($('#rozniceprice').val()*(1-(-mult_opt/100))/10)*10);
                };
            };
        };
    };
    function print_prices(){
        var optprice = $('#optprice').val();
        var rozniceprice = $('#rozniceprice').val();
        var oneprice = $('#oneprice').val();
        $('#containermain').append('<div class="row" style="padding-left: 15px;padding-right: 15px;"><div class="col-xs-4" style="padding-left: 0px;padding-right: 0px;"><p>'+optprice+'</p></div><div class="col-xs-4" style="padding-left:0px;padding-right: 0px;"><p>'+rozniceprice+'</p></div><div class="col-xs-4" style="padding-left:0px;padding-right: 0px;"><p>'+oneprice+'</p></div></div>');
    };
    $(document).on('change', '#selecttype', function() {
        $('#modifroznica').val($(this).find('option:selected').attr('data-roznica'));
        $('#modifopt').val($(this).find('option:selected').attr('data-opt'));
        if ($('#minprice').val()!= null)
        {
            $('#minprice').val($(this).find('option:selected').attr('data-min_price'));
        }
        else
        {
            $('#minprice').val("");
        }
        update_prices();
    });

    $(document).on('change', '#modifroznica', function() {
        update_prices();
    });
    $(document).on('change', '#modifopt', function() {
        update_prices();
    });
    $(document).on('change', '#oneprice', function() {
        update_prices();
        print_prices();
    });
    $(document).on('change', '#totalprice', function() {
        $('#oneprice').val($(this).val()/$('#amount').val());
        update_prices();
    });
    $(document).on('change', '#amount', function() {
        $('#oneprice').val($('#totalprice').val()/$(this).val());
        update_prices();
    });
    
        
});