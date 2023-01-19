from django.urls import path
from my_app.views import article, article_archive, article_slug, another, main_article

urlpatterns = [
    path('', another),
    path('arhive/', main_article),
    path('<int:article_number>', article),
    path('<int:article_number>/archive', article_archive),
    path('<int:article_number>/<slug:slug_text>', article_slug),
]