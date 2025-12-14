from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm


def forum_home(request):
    posts = Post.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'forum/home.html', {'items': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user          
            post.is_approved = request.user.is_staff 
            post.save()
            return redirect('forum-home')
    else:
        form = PostForm()

    return render(request, 'forum/create_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=True)
    comments = Comment.objects.filter(post=post, is_approved=True)

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.is_approved = request.user.is_staff
            comment.save()
            return redirect('post-detail', pk=pk)
    else:
        form = CommentForm()

    return render(
        request,
        'forum/post_detail.html',
        {
            'post': post,
            'form': form,
            'comments': comments
        }
    )


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return redirect('forum-home')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'forum/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and not request.user.is_staff:
        return redirect('forum-home')

    if request.method == "POST":
        post.delete()
        return redirect('forum-home')

    return render(request, 'forum/delete_post.html', {'post': post})


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        return redirect('forum-home')

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'forum/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author and not request.user.is_staff:
        return redirect('forum-home')

    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post-detail', pk=post_pk)

    return render(request, 'forum/delete_comment.html', {'comment': comment})


@login_required
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=True)
    post.upvotes += 1
    post.save()
    return redirect('post-detail', pk=pk)


@login_required
def downvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=True)
    post.downvotes += 1
    post.save()
    return redirect('post-detail', pk=pk)
