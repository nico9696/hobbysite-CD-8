from django import forms
from django.forms import inlineformset_factory
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
        widgets = {
            'entry': forms.Textarea(attrs={'class': 'article-textarea'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'article-file'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        labels = {'entry': ''}
        
        widgets = {'entry': forms.Textarea(attrs={
            'class': 'comment-textarea',
            'placeholder': 'Add a comment...'
        })}
