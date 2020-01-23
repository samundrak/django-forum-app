from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Posts
from comments.models import Comments
from django.contrib.auth.models import User
from .forms import ProfileForm, ProfilePasswordForm
from django.contrib import messages


def change_password(request):
    instance = get_object_or_404(User, id=request.user.id)
    if not instance or not request.user.is_authenticated:
        return redirect('/')

    form = ProfilePasswordForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Profile has been updated.")
        return redirect('/profile/' + str(instance.id))

    return render(request, 'registration/password.html', {
        'form': form
    })


# Create your views here.
def edit_profile(request):
    instance = get_object_or_404(User, id=request.user.id)
    if not instance or not request.user.is_authenticated:
        return redirect('/')

    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Profile has been updated.")
        return redirect('/profile/' + str(instance.id))

    return render(request, 'profile-edit.html', {
        'form': form
    })


def profile(request, id):
    userId = get_object_or_404(User, id=id)
    instance = get_object_or_404(User, id=id)
    posts = Posts.objects.filter(user=id).values('id', 'title').order_by(
        '-created_at')
    comments = Comments.objects.filter(user=id).values('id', 'content', 'post_id').order_by(
        '-created_at')
    return render(request, 'profile.html', {
        'profile': instance,
        'comments': comments,
        'posts': posts
    })
