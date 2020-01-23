"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from posts import views as postView
from register import views as registerView
from comments import views as commentView
from users import views as user_view
from django.urls import path, include

urlpatterns = [
    path('', postView.home_view),
    path('search/', postView.home_view),
    path('profile/<int:id>', user_view.profile),
    path('profile/edit', user_view.edit_profile),
    path('password/', user_view.change_password),
    path('register', registerView.register_view),
    path('', include('django.contrib.auth.urls')),
    path('posts/<int:id>', postView.post_single),
    path('posts/create', postView.post_create),
    path('posts/delete/<int:id>', postView.post_delete),
    path('posts/edit/<int:id>', postView.post_edit),
    path('posts/<int:post_id>/comment', commentView.comment_resource),
    path('comment/<int:comment_id>/delete', commentView.delete_comment)
]
