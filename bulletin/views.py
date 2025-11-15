from django.shortcuts import render, get_object_or_404, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required

def bulletin_home(request):
    items = Announcement.objects.order_by('-date_posted')
    return render(request, 'bulletin/home.html', {'announcements': items})

@login_required
def add_announcement(request):
    if request.method=='POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.posted_by = request.user
            obj.save()
            return redirect('bulletin-home')
    else:
        form = AnnouncementForm()
    return render(request, 'bulletin/form.html', {'form': form})

@login_required
def edit_announcement(request, pk):
    ann = get_object_or_404(Announcement, pk=pk)
    if request.method=='POST':
        form = AnnouncementForm(request.POST, instance=ann)
        if form.is_valid():
            form.save()
            return redirect('bulletin-home')
    else:
        form = AnnouncementForm(instance=ann)
    return render(request, 'bulletin/form.html', {'form': form})
