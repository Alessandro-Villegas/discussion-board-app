from django.shortcuts import render
from .models import Post

def home(request):
    # get posts from database
    items = Post.objects.all()
    return render(request, 'forum/home.html', {'items': items})
