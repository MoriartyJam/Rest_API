from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new post...'}))

    class Meta:
        model = Post
        fields = ('title', 'content',)






