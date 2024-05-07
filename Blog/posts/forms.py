from django import forms
from tinymce.widgets import TinyMCE

from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
   
    content = forms.CharField(widget=TinyMCE(attrs={'id': 'id_content'}))
    
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
       
    class Meta:
        model = Comment
        fields = ['text']
