from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog
from posts.models import Post

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'create-blog.html', {'form': form})

def blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs-list.html', {'blogs': blogs})

def blog_detail(request, pk):
     blog = get_object_or_404(Blog, pk=pk)
     posts = Post.objects.filter(blog=blog)
     if request.method == 'POST' and 'delete_blog' in request.POST:
        blog.delete()
        return redirect('blogs_list') 
     return render(request, 'blog-detail.html', {'blog': blog, 'posts': posts})

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs_list') 
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog-update.html', {'form': form})

