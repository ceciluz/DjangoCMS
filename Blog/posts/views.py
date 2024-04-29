from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from create_blog.views import blog_detail
# Create your views here.

def create_post(request, id_blog):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog_id = id_blog
            post.save()
            return redirect('posts:post_detail', id_blog=id_blog, id_post=post.pk)
            print("Done")
    else:
        form = PostForm()
        print("FAILED")
    return render(request, 'create-post.html', {'form': form})

def post_detail(request, id_blog, id_post):
    post = get_object_or_404(Post, id=id_post)

    if request.method == 'POST' and 'delete_post' in request.POST:
        post.delete()
        return redirect('blog_detail', pk=id_blog)  
    return render(request, 'post-detail.html', {'post': post})

def post_update(request, id_blog, id_post):
    post = get_object_or_404(Post, pk=id_post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', id_blog=id_blog, id_post=id_post)
    else:
        form = PostForm(instance=post)

    return render(request, 'post-update.html', {'form': form})