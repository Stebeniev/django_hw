from django.shortcuts import render
from site_blog.models import Comment


def comments(request):
    data = {
        'comments': Comment.objects.order_by('-created_at')[:5]
    }
    return render(request, 'comments.html', data)


def create(request):
    data = {
        'comments': Comment.objects.filter()[6:11]
    }
    return render(request, 'create.html', data)


def update(request):
    data = {
        'comments': Comment.objects.filter()[8:11]
    }
    return render(request, 'update.html', data)



def delete(request):
    filter_comments = Comment.objects.filter(body__icontains='k').exclude(body__icontains='c')
    data = {
        'comments': filter_comments.delete()
    }
    return render(request, 'delete.html', data)

