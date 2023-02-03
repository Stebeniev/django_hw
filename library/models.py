from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.first_name


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    users = models.ManyToManyField(User)
    issued = models.DateField(null=True, blank=True)
    availability = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'book'
        verbose_name_plural = 'books'


    def __str__(self):
        return self.name


class RegistrationCard(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_issue = models.DateField(null=True)
    return_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.book} {self.user} {self.date_of_issue} {self.return_date}'


