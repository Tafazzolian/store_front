from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from django.db.models.functions import Concat
from store.models import Product, Customer, OrderItem, Order, Collection

#query testing
def say_hello(request):
    last_order_id = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField()) 
    query_set = Product.objects.annotate(
        money_spent=Sum(F('orderitem__unit_price')*F('orderitem__quantity'))).order_by('-money_spent')[:5]
    m1 = Product.objects.aaggregate(Max('price'))

    return render(request, 'hello.html', {'queryset': query_set})