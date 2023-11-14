from django.shortcuts import render
from .models import *


def main_page(request):
    news = New.objects.all()

    context = {'title': 'Main Page',
               'news': news}

    return render(request, 'show_info/main_page.html', context)


def category_page(request, category):
    category_post = New.objects.filter(category__name=category)

    context = {'title': 'Category',
               'category_post': category_post}

    return render(request, 'show_info/category_page.html', context)


def show_post(request, post_slug):
    post = New.objects.get(slug=post_slug)

    context = {'title': 'Post',
               'post': post}

    return render(request, 'show_info/show_post.html', context)
