from django.urls import path

from site_blog.views import comments, delete, create, update

urlpatterns = [
    path('comments/', comments, name='comments'),
    path('create/', create, name='create'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),

]