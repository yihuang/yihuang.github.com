from django import forms
from models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'snippet': forms.HiddenInput,
            'lineno': forms.HiddenInput,
        }
