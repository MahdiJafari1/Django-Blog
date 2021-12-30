from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        exclude = ('post',)
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment'
        }
