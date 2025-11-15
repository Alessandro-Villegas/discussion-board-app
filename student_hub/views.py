from django.shortcuts import render
from forum.models import Post

def student_hub_home(request):
    return render(request, 'student_hub/home.html')