from datetime import date
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Tag, Author
from django.shortcuts import get_object_or_404, render

class HomeView(TemplateView):
    template_name = "blog/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-date')[:3]
        return context
    
class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/posts.html'


class PostDetail(DetailView):
    model = Post
    template_name='blog/post_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slug"] = self.kwargs['slug']
        return context
