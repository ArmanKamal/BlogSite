from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


    


def about(request):
    return render(request,'blog/about.html')