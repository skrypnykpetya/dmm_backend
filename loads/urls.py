from django.urls import path

from . import views

urlpatterns = [
    path('get_items/', views.get_items),
    path('get_completed_items/', views.get_completed_items),
    path('set_status/', views.set_status),
    path('get_status/', views.get_status),
]