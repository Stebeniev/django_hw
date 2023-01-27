from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name

    ordering = ['first_name']
    verbose_name = 'author'
    verbose_name_plural = 'authors'


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'book'
        verbose_name_plural = 'books'

