from django.urls import path
from .views import notebooks, asus,acer

urlpatterns = [
    path('', notebooks, name="notebooks"),
    path('asus', asus, name="asus"),
    path('acer', acer, name="acer"),
]