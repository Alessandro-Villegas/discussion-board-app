from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Activity
from .forms import ActivityForm
from django.utils import timezone
import datetime

@login_required
def schedule_home(request):
    activities = Activity.objects.filter(user=request.user)
    # upcoming for notifications (next 24h)
    now = timezone.now()
    # create datetime for activities this week (approx)
    upcoming = []
    for a in activities:
        # compute next occurrence date for the activity (simple approach)
        today = now.date()
        weekday_index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'].index(a.day_of_week)
        days_ahead = (weekday_index - now.weekday() + 7) % 7
        next_date = today + datetime.timedelta(days=days_ahead)
        dt = datetime.datetime.combine(next_date, a.start_time)
        dt = timezone.make_aware(dt, timezone.get_current_timezone())
        upcoming.append({'id':a.pk, 'title':a.title, 'datetime': dt.isoformat(), 'description': a.description})
    return render(request, 'schedule/home.html', {'activities': activities, 'upcoming': upcoming})

@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('schedule-home')
    else:
        form = ActivityForm()
    return render(request, 'schedule/activity_form.html', {'form': form, 'mode':'Add'})

@login_required
def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('schedule-home')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'schedule/activity_form.html', {'form': form, 'mode':'Edit', 'activity': activity})

@login_required
def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk, user=request.user)
    if request.method == 'POST':
        activity.delete()
        return redirect('schedule-home')
    return render(request, 'schedule/delete_activity.html', {'activity': activity})

