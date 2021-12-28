from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post, Tag, Author

def home(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/home.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/posts.html')

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_details.html', {
        'post': post
    })