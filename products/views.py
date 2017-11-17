from django.shortcuts import render
from products.models import *
from orders.models import *
from django.http import JsonResponse, HttpResponseRedirect
from decimal import *
from django.db.models import Sum
from orders.form_basket_uot import Checkout_contact_form


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    return_dict['session_key'] = session_key

    data = request.POST

    product_id = data.get('product_id')

    is_delete = data.get('is_delete')
    print(data)
    if is_delete == 'true':
        print(is_delete)
        prod, is_create = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id)
        prod.is_active = False
        prod.save(force_update=True)
    else:
        nmb = int(data.get('nmb'))
        price = Decimal(data.get('price'))
        total_amount = nmb * price
        new_prod, is_create = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                    defaults={'numb': nmb})
        if not is_create:
            if new_prod.is_active == True:
                new_prod.numb += nmb
            else:
                new_prod.numb = nmb
                new_prod.is_active = True
            new_prod.save(force_update=True)

    kvo_prod = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    return_dict['products_total_nmb'] = kvo_prod.count()
    products_total_amount = kvo_prod.aggregate(Sum('total_amount'))
    products_total_amount = products_total_amount['total_amount__sum']
    return_dict['products_total_amount'] = products_total_amount

    return_dict['products'] = list()

    for prod in kvo_prod:
        prod_dict = dict()
        prod_dict['product_id'] = prod.product.id
        prod_dict['name'] = prod.product.name
        prod_dict['price_per_item'] = prod.price
        prod_dict['nmb'] = prod.numb
        return_dict['products'].append(prod_dict)

    return JsonResponse(return_dict)


def product_(request, product_id):
    product = Products.objects.filter(id=product_id)
    item_product = product[0]
    foto_product = Spisok_foto.objects.filter(product=item_product)
    return render(request, "product.html", locals())


def chek_out(request):
    form = Checkout_contact_form(request.POST or None)
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_amount = products_in_basket.aggregate(Sum('total_amount'))
    products_total_amount = products_total_amount['total_amount__sum']
    print(request.POST)
    if request.POST:
        if form.is_valid():
            # form.is_valid()
            data = request.POST
            name = data.get("name")
            phone = data["phone"]
            adress = data["adress"]
            comment = data["comment"]
            post_office = data["optionsPost"]
            comment += " , " + post_office
            #  user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(customer_name=name, customer_phone=phone, customer_adress=adress,
                                         coments=comment)

            order_in_session = OrderInSession.objects.create(session_key=session_key, order=order)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(product_id=product_in_basket_id)
                    product_in_basket.numb = int(value)
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, numb=product_in_basket.numb,
                                                  price=product_in_basket.product.price, order=order)
            products_in_basket.delete()
            products_in_basket = 'ЗАКАЗАЛИ'
            products_total_amount = order.id
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        
        else:
            print("no")
        
    return render(request, "checkout.html", locals())
