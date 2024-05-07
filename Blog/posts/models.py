from django.db import models
from django.utils import timezone
from create_blog.models import Blog
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
