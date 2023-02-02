# from django.http import HttpResponse
from django.shortcuts import render
from random import randrange, randint


# def main(request):
#     return HttpResponse("Hi! It's your main view!!")
#
#
# def another(request):
#     return HttpResponse("Hi, It's another page!!")
#
#
# def main_article(request):
#     return HttpResponse('Hi, There will be a list with articles')
#
#
# def main_new(request):
#     return HttpResponse("Hi! Users!!")
#
#
# def article(request, article_number):
#     return HttpResponse(f"Hi, {article_number} article")
#
#
# def article_archive(request, article_number):
#     return HttpResponse(f"Hi, {article_number} article, archive")
#
#
# def article_slug(request, article_number, slug_text):
#     return HttpResponse(f"Hi, {article_number}  {slug_text} ")
#
#
# def user_number(request, number):
#     return HttpResponse(f"Hi, {number}")
#
#
# def regex(request, text):
#     return HttpResponse(f"Hi, it's regex with text: {text}")
#
#
# def valid(request, num):
#     return HttpResponse(f"The number- {num} - is a valid number")
#
#
# def invalid(request, num):
#     return HttpResponse(f"The number- {num} - is an invalid number")
#

def main(request):
    return render(request, 'main.html')


def first(request):
    data = {
        'article_number': randint(0, 100),

    }
    return render(request, 'first.html', data)


def article(request, article_number, slug_text=""):
    return render(request, 'article.html', {'article_number': article_number, 'slug_text': slug_text})


