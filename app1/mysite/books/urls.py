from django.urls import path
from .views import books_genre, books_list, books_after

urlpatterns = [
    path('', books_genre, name="books-genre"),
    path('list/', books_list, name="books-list"),
    path('after/', books_after, name="books-after")
]