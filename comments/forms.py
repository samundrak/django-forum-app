from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Comments
        fields = ['content']
