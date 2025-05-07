from django import forms
from .models import Thread, Comment, ThreadCategory

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

class ThreadCategoryForm(forms.ModelForm):
    class Meta:
        model = ThreadCategory
        fields = ['name', 'description']