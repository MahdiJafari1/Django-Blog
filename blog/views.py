from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from .models import Comment, Post, Tag, Author
from .forms import CommentForm
from django.urls import reverse
from django.shortcuts import render

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

class PostDetailsView(View):
    def get(self, request, slug, *args, **kwargs):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'tags': post.tags.all(),
            'form': CommentForm(),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post_details.html', context)
    
    
    def post(self, request, slug, *args, **kwargs):
        comment = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment.is_valid():
            comment.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_details', args=[slug]))
        
        context = {
            'post': post,
            'tags': post.tags.all(),
            'form': CommentForm()
        }
        return render(request, 'blog/post_details.html', context)