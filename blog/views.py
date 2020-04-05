from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [

{
    'author': 'Arman',
    'title': 'Blog Post 1',
    'content':  'First Post content',
    'date_posted': 'August 27,2014'
},

{
    'author': 'Arman',
    'title': 'Blog Post 1',
    'content':  'First Post content',
    'date_posted': 'August 27,2014'
},

{
    'author': 'Arman',
    'title': 'Blog Post 1',
    'content':  'First Post content',
    'date_posted': 'August 27,2014'
},


]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')