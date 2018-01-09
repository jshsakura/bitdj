from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    user = request.user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(Coalesce('published_date','created_date').desc())
    return render(request, 'blog/post_list.html', {'posts': posts,'user': user})


def contact(request):

    return render(request, 'blog/contact.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    user = request.user
    return render(request, 'blog/post_new.html', {})
