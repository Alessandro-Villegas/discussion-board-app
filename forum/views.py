from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    items = Post.objects.all()
    return render(request, 'forum/home.html', {'items': items})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'forum/post_detail.html', {'post': post, 'form': form, 'comments': comments})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user.username != post.author:
        return redirect('forum-home')
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'forum/edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        post.delete()
        return redirect('forum-home')
    
    return render(request, 'forum/delete_post.html', {'post': post})

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user.username != comment.author:
        return redirect('forum-home')
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'forum/edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post-detail', pk=post_pk)
    
    return render(request, 'forum/delete_comment.html', {'comment': comment})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum-home')  
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})