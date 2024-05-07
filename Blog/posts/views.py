from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from create_blog.views import blog_detail
from django.contrib import messages
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
    comments = post.comments.all() if post.comments.exists() else []
    
    if request.method == 'POST':
        if 'delete_post' in request.POST:
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('blog_detail', pk=id_blog)
        
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('posts:post_detail', id_blog=id_blog, id_post=id_post)

        comment_id = request.POST.get('comment_id')
        if comment_id:
            comment_to_edit = get_object_or_404(Comment, id=comment_id)
            if comment_to_edit.user == request.user:
                if 'edit_comment' in request.POST:
                   return redirect('posts:edit_comment', id_blog=id_blog, id_post=id_post, comment_id=comment_id)
                elif 'delete_comment' in request.POST:
                    comment_to_edit.delete()
                    messages.success(request, 'Comment deleted successfully.')
                    return redirect('posts:post_detail', id_blog=id_blog, id_post=id_post)
    
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'post-detail.html', context)

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

def edit_comment(request, id_blog, id_post, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:post_detail', kwargs={'id_blog': id_blog, 'id_post': id_post}))
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.post.author != request.user and comment.user != request.user:
        return redirect('post_detail', id_blog=comment.post.id_blog, id_post=comment.post.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', id_blog=comment.post.id_blog, id_post=comment.post.id)

    return render(request, 'comment_delete.html', {'comment': comment})