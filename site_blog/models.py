from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')
    text = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['author', 'text']

    def __str__(self):
        return 'Post by {} on {}'.format(self.author, self.text)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('site_blog.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['text', 'user']

    def __str__(self):
        return "{} by {}".format(self.text, self.user.username)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return "{} by {}".format(self.user.username, self.post.id)