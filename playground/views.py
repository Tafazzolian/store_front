from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Concat
from store.models import Product, Customer, OrderItem, Order, Collection
from tags.models import TaggedItem

#query testing
def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)
    query_set = TaggedItem.objects\
        .select_related('tag')\
        .filter(
        content_type=content_type,
        object_id = 6,
        )

    return render(request, 'hello.html', {'queryset': query_set})