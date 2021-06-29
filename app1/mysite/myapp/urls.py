from django.urls import path
from .views import index_page, page_second, first_name, last_name

urlpatterns = [
    path('', index_page, name="index-page"),
    path('second/', page_second, name="second-page"),
    path('first/',  first_name, name="first-name"),
    path('last/', last_name, name="last-name"),
]