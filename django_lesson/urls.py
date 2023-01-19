from django.urls import path, re_path, include
from my_app.views import main, main_new, user_number, regex, valid, invalid

urlpatterns = [
    path('', main),
    path('users', main_new),
    path('article/', include('my_app.urls')),
    path('users/<int:user_number>', user_number),
    re_path(r'^(?P<text>[0-9a-fA-F]{4}-[0-9a-fA-F]{6}/$)', regex),
    re_path(r'^(?P<num>050\d{7}|[1,3,5,7]d{7}$)', valid),
    re_path(r'^(?P<num>075\d{7}|[2,4,6,8]d{7}$)', invalid),
    # path('article/', another),
    # path('article/arhive/', main_article),
    # path('article/<int:article_number>', article),
    # path('article/<int:article_number>/archive', article_archive),
    # path('article/<int:article_number>/<slug:slug_text>', article_slug),
]
