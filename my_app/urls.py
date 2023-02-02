from django.urls import path
# from my_app.views import article, article_archive, article_slug, another, main_article
from .views import main, first, article

urlpatterns = [
    # path('', another),
    # path('archive/', main_article),
    # path('article/<int:article_number>', article),
    # path('article/<int:article_number>/archive', article_archive),
    # path('article/<int:article_number>/<slug:slug_text>', article_slug),

    path('', main, name='main'),
    path('first/', first, name='first'),
    path('article/<int:article_number>/', article, name='article'),
    path('article/<int:article_number>/<slug:slug_text>', article, name='slug_text'),


]