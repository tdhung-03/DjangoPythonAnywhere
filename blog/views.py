from django.shortcuts import render
from .models import *


# Create your views here.

def list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "list.html", context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post": post
    }
    return render(request, "post.html", context)
