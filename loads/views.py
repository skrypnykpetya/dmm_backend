from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import *

DRIVER_STATUS = {
    'planned': (2, 'onLoad', 'Delivering'),
    'pickUp': (3, 'Delivering', 'on Delivery'),
    'delivering': (4, 'on Delivery', 'Loaded'),
    'delivery': (5, 'Loaded', 'completed'),
    'completed': (5, 'completed', 'completed')
}

@api_view(['GET'])
def get_items(request):
    user = request.user
    driver = Drivers.objects.get(user=user)
    items = Loads.objects.filter(driver=driver)
    data = prepare_items(items)

    return JsonResponse(data, status=200, safe=False)

@api_view(['POST'])
def set_status(request):
    user = request.user
    order = request.data.get('order')
    driver = Drivers.objects.get(user=user)
    load = Loads.objects.get(driver=driver, order_number=order)
    status = DRIVER_STATUS[load.driver_status]
    if status[1] == 'Loaded':
        load.delivery_status = 'cancelled'

    load.driver_status = status[0]
    load.save()

    return JsonResponse({'status': load.driver_status, 'action': status[2]}, status=200)

@api_view(['POST'])
def get_status(request):
    user = request.user
    order = request.data.get('order')
    driver = Drivers.objects.get(user=user)
    load = Loads.objects.get(driver=driver, order_number=order)
    status = DRIVER_STATUS[load.driver_status]

    return JsonResponse({'status': load.driver_status, 'action': status[1]}, status=200)


def prepare_items(items):
    data = []
    for item in items:
        if item.driver_status == 'completed':
            continue

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
