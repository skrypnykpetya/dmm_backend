from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from api.models import *

@api_view(['GET'])
def get_items(request):

    items = Loads.objects.all()
    data = prepare_items(items)

    return JsonResponse(data, status=200, safe=False)


def prepare_items(items):
    data = []
    for item in items:
        data.append({
            'driver': f"{item.driver.first_name} {item.driver.last_name}",
            'trailer': item.trailer.model,
            'customer': item.customer.name,
            'pickup_address': item.pickup_address.address,
            'delivery_address': item.delivery_address.address,
            'order_number': item.order_number,
            'distance': item.distance,
            'price': item.price,
            'pickup_date': item.pickup_date,
            'delivery_date': item.delivery_date,
            'pickup_time': item.pickup_time,
            'delivery_time': item.delivery_time,
            'delivery_status': item.delivery_status,
            'payment_status': item.payment_status,
            'driver_status': item.driver_status
        })
    return data
