from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Posts
from django.contrib import messages


# Create your views here.
def home_view(request):
    query = request.GET.get('query')
    mode_query = Posts.objects
    if query:
        mode_query = mode_query.filter(title__contains=query, content__contains=query)

    posts = mode_query.all().order_by('-created_at')
    return render(request, 'index.html', {
        'posts': posts,
        'query': query or ''
    })


def post_single(request, id):
    post = Posts.objects.all().filter(id=id).first()
    return render(request, 'posts/single.html', {
        'post': post
    })


def post_delete(request, id):
    post = Posts.objects.all().filter(user=request.user, id=id)
    print(post)
    if len(post) == 0:
        messages.warning(request, "Unauthorized access!")
        return redirect('/')
    post.delete()
    messages.success(request, "Post has been deleted.")
    return redirect('/')


def post_edit(request, id):
    instance = get_object_or_404(Posts, id=id)
    if not instance:
        return redirect('/')

    if instance.user_id != request.user.id:
        return redirect('/')

    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post has been updated.")
        return redirect('/posts/' + str(instance.id))
    context = {
        'title': 'Edit',
        'form': form
    }
    return render(request, 'posts/create.html', context)


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
        "form": form,
        'title': 'Add'
    })
