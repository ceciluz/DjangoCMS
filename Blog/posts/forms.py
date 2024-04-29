from django import forms
from tinymce.widgets import TinyMCE

from .models import Post

class PostForm(forms.ModelForm):
   
    content = forms.CharField(widget=TinyMCE(attrs={'id': 'id_content'}))
    
    class Meta:
        model = Post
        fields = ['title', 'content']
