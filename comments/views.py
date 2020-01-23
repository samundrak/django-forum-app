from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comments
from posts.models import Posts
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def comment_resource(request, post_id):
    if request.method != 'POST':
        return comments_all(request, post_id)
    if not request.user.is_authenticated:
        return redirect('/')
    form = CommentForm(request.POST or None)
    comment = form.save(commit=False)
    comment.user = request.user
    comment.post_id = post_id
    comment.save()
    nextComment = Comments.objects.get(id=comment.id)
    nextComment.user = request.user
    serialized_obj = serializers.serialize('json', [nextComment])

    return JsonResponse({'c': serialized_obj})


def comments_all(request, post_id):
    comments = Comments.objects.filter(post_id=post_id).select_related('user').values('id',
                                                                                      'content',
                                                                                      'post_id',
                                                                                      'created_at',
                                                                                      'user__id',
                                                                                      'user__username',
                                                                                      'user__first_name',
                                                                                      'user__last_name').order_by(
        '-created_at')
    return JsonResponse({'comments': list(comments)})


def delete_comment(request, comment_id):
    instance = get_object_or_404(Comments, id=comment_id)
    if request.method != 'POST' or not request.user.is_authenticated:
        return redirect('/')

    if not instance:
        return JsonResponse({'success': False})
    instance.delete()
    return JsonResponse({'success': True})
