from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from django.db.models.functions import Concat
from store.models import Product, Customer, OrderItem, Order, Collection

#query testing
def say_hello(request):
    query_set = Customer.objects.annotate(result = Max('order__id'))

    return render(request, 'hello.html', {'queryset': query_set})