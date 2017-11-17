from orders.models import ProductInBasket, OrderInSession
from django.db.models import Sum

def get_basket_kvo(request):
    return_dict = dict()
    session_key = request.session.session_key
    return_dict['session_key'] = session_key

    prod_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = prod_in_basket.count()
    products_total_amount = prod_in_basket.aggregate(Sum('total_amount'))
    products_total_amount = products_total_amount['total_amount__sum']

    if len(prod_in_basket) == 0:
        order_in_session = OrderInSession.objects.filter(session_key=session_key)

    return locals()