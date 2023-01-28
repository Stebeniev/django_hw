from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        ordering = ['name']
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.name



