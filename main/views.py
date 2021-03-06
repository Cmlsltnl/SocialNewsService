# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from posts.models import Post, Category
from user_profile.models import UserProfile
from .forms import RegisterForm
from django.shortcuts import get_object_or_404
from posts.views import count_comments, show_posts

from django.template.loader import render_to_string


def home(request):
    posts_response = show_posts(request)
    context = {'posts_response': posts_response}
    return render(request, "main/home.html", context)


@login_required()
def upvote_news(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.votes += 1
    post.save()
    return redirect("/")


@login_required()
def downvote_news(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.votes -= 1
    post.save()
    return redirect("/")


def category_filter(request, pk):
    posts = Post.objects.filter(category__id=pk)
    category = Category.objects.get(id=pk)
    context = {'posts': posts, 'category': category}
    return render(request, "main/home.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user_profile = UserProfile()
            user_profile.user = User.objects.get(username=form.data['username'])
            user_profile.save()
            return redirect('login')
    else:
        form = RegisterForm
    return render(request, "main/register.html", {'form': form})
