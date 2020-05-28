from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'James Vick',
        'title': 'Django Blog Post',
        'content': ' This is a Django blog post',
        'date_posted': 'May 28, 2020'
    },
    {
        'author': 'Tony Ferguson',
        'title': 'Another Django Blog Post',
        'content': ' This is another Django blog post',
        'date_posted': 'May 28, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
