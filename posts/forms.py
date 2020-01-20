from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    title = forms.TextInput()
    content = forms.Textarea()

    class Meta:
        model = Posts
        fields = ['title', 'content']
