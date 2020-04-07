from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
#     posts = Post.objects.all()
    
#     return render(request, 'blog/home.html',{'posts':posts})



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']   

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


def about(request):
    return render(request,'blog/about.html')