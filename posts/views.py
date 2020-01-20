from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Posts
from django.contrib import messages


# Create your views here.
def home_view(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('/')

    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "New post has been added.")
            return redirect('/')

    return render(request, 'posts/create.html', {
        "form": form
    })
