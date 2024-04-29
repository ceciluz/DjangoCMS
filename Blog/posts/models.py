from django.db import models
from django.utils import timezone
from create_blog.models import Blog
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
