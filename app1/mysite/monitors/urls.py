from django.urls import path
from .views import monitors, hp_monitor, dell_monitor

urlpatterns = [
    path('', monitors, name="monitors"),
    path('hp_monitor', hp_monitor, name="hp_monitor"),
    path('dell_monitor', dell_monitor, name="dell_monitor"),
]