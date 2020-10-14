from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def snake(request):
    return render(request, 'base/snake.html')

def present(request):
    return render(request, 'base/present.html')

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
    return render(request, 'base/index.html', context)


def posts(request):
    posts = Post.objects.filter(active=True)

    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'base/post.html', context)


def profile(request):
    return render(request, 'base/profile.html')

