from django.contrib import admin
from .models import Author, Post, Comment, Like

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

