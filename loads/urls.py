from django.urls import path

from . import views

urlpatterns = [
    path('get_items/', views.get_items),
]