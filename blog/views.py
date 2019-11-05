from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'BillyTwoShoes',
        'title': 'Primero Post',
        'content': 'Hello world! (From first dictionary entry)',
        'date_posted': '11.4.2019'
    },
    {
        'author': 'BillyTwoShoes',
        'title': 'Post Deux',
        'content': 'Hello world! (From second dictionary entry)',
        'date_posted': '11.5.2019'
    }
]

# Create your views here.
def home(request):
    context ={
        'posts':  Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':  'About'})