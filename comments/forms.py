# _*_ coding: utf-8 _*_
__aythor__ = 'Anson'
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']