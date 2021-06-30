from django.urls import path
from .views import home, author, genre, book, book_details, author_details

urlpatterns = [
   path('', home, name="home-page"),
   path('authors/', author, name="author-page"),
   path('authors/<int:author_id>/', author_details, name="author_details"),
   path('genres/', genre, name="genre-page"),
   path('book/', book, name="book-page"),
   path('book/<int:book_id>/', book_details, name="book_details"),
]