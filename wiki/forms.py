from django import forms
from django.forms import inlineformset_factory
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
