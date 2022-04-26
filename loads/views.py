from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import *

DRIVER_STATUS = {
    'planned': {
        'status': 'planned',
        'next_status': 'pickUp',
        'next_status_id': 2,
        'action': 'onLoad',
        'next_action': 'Delivering'
    },
    'pickUp': {
        'status': 'pickUp',
        'next_status': 'delivering',
        'next_status_id' : 3,
        'action': 'Delivering',
        'next_action': 'on Delivery'
    },
    'delivering': {
        'status': 'delivering',
        'next_status': 'delivery',
        'next_status_id': 4,
        'action': 'on Delivery',
        'next_action': 'Loaded'
    },
    'delivery': {
        'status': 'delivery',
        'next_status': 'completed',
        'next_status_id': 5,
        'action': 'Loaded',
        'next_action': 'completed'
    },
    'completed': {
        'status': 'completed',
        'next_status': 'completed',
        'next_status_id': 5,
        'action': 'completed',
        'next_action': 'completed'}
}

@api_view(['GET'])
def get_items(request):
    user = request.user
    driver = Drivers.objects.get(user=user)
    items = Loads.objects.filter(driver=driver)
    data = prepare_items(items)

    return JsonResponse(data, status=200, safe=False)

@api_view(['GET'])
def get_completed_items(request):
    user = request.user
    driver = Drivers.objects.get(user=user)
    items = Loads.objects.filter(driver=driver, delivery_status='cancelled')
    data = prepare_items(items, completed=True)

    return JsonResponse(data, status=200, safe=False)

@api_view(['POST'])
def set_status(request):
    user = request.user
    order = request.data.get('order')
    driver = Drivers.objects.get(user=user)
    load = Loads.objects.get(driver=driver, order_number=order)
    status = DRIVER_STATUS[load.driver_status]
    if status['action'] == 'Loaded':
        load.delivery_status = 'cancelled'

    load.driver_status = status['next_status_id']
    load.save()

    return JsonResponse({'status': status['next_status'], 'action': status['next_action']}, status=200)

@api_view(['POST'])
def get_status(request):
    user = request.user
    order = request.data.get('order')
    driver = Drivers.objects.get(user=user)
    load = Loads.objects.get(driver=driver, order_number=order)
    status = DRIVER_STATUS[load.driver_status]

    return JsonResponse({'status': status['status'], 'action': status['action']}, status=200)


def prepare_items(items, completed=False):
    data = []

    for item in items:

        if not completed:
            if item.delivery_status == 'cancelled':
                continue
        elif completed:
            if item.delivery_status != 'cancelled':
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
