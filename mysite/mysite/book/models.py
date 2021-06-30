from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    age = models.SmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.first_name}"" "f"{self.last_name}"


class Genre(models.Model):
    genre_name = models.CharField(max_length=90, blank=False, null=False)

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    genre_name = models.ForeignKey(Genre, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
