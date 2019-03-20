from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'sam',
        'title': 'blog 1',
        'content': 'content 1',
        'date_posted': 'today'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')