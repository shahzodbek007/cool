from django.urls import path
from .views import smartphones, samsung, apple

urlpatterns = [
    path('', smartphones, name="smartphones"),
    path('samsung', samsung, name="samsung"),
    path('apple', apple, name="apple"),
]