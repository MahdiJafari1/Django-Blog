from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    return render(request, 'blog/posts.html')

def post_detail(request):
    pass    