from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class ProfileForm(UserChangeForm):
    email = forms.EmailField()
    firstName = forms.TextInput()
    lastName = forms.TextInput()

    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'email']


class ProfilePasswordForm(PasswordChangeForm):
    old_password = forms.TextInput()
    new_password1 = forms.TextInput()
    new_password2 = forms.TextInput()

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
