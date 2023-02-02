from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class Author(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')
    text = models.TextField(max_length=10000, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Author - {}, id - {}".format(self.author.name, self.id)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey('site_blog.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                     related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # class Meta:
    #     unique_together = ['text', 'user']

    def __str__(self):
        return "{} by {}".format(self.text, self.user.username)

# class Comment(models.Model):

    # post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255, null=True, blank=True)
    # body = models.TextField(max_length=10000, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255, null=True, blank=True)
    # body = models.TextField(max_length=10000, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # comment = models.ForeignKey('site_blog.Comment', on_delete=models.CASCADE, default="", null=True,
    #                             blank=True, related_name="comments")
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, default="")

    # def __str__(self):
    #     return "{} by {}".format(self.post, self.user.username)

    def save(self, **kwargs):
        if not self.id:
            self.created_at = timezone.now() - timedelta(days=365)
        super().save(**kwargs)




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return "{} by {}".format(self.user.username, self.post.id)
