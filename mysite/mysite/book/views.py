from django.shortcuts import render
from .models import Author, Genre, Book


def home(request):
    return render(request, "home.html")


def author(request):
    authors = Author.objects.all()
    ctx = {
        "authors": authors
    }
    return render(request, "author-list.html", ctx)


def author_details(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.filter(author_id=author_id)
    ctx = {
        "author": author,
        "book": book
    }
    return render(request, "author_details.html", ctx)


def genre(request):
    genres = Genre.objects.all()
    ctx = {
        "genres": genres
    }
    return render(request, "genre-list.html", ctx)


def book(request):
    books = Book.objects.all()
    ctx = {
        "books": books
    }
    return render(request, "book-list.html", ctx)


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    ctx = {
        "book": book
    }
    return render(request, "book-details.html", ctx)



