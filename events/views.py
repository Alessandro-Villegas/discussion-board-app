from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Subscription
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse

def events_list(request):
    events = Event.objects.order_by('date','time')
    return render(request, 'events/calendar.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {'event': event})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            ev = form.save(commit=False)
            ev.created_by = request.user
            ev.save()
            return redirect('events-list')
    else:
        form = EventForm()
    return render(request, 'events/form.html', {'form': form})

@login_required
def subscribe_category(request, category):
    if request.method=='POST':
        Subscription.objects.get_or_create(user=request.user, category=category)
    return redirect('events-list')

@login_required
def unsubscribe_category(request, category):
    Subscription.objects.filter(user=request.user, category=category).delete()
    return redirect('events-list')

# JS calendar will request events via JSON
def events_json(request):
    qs = Event.objects.all()
    items = []
    for e in qs:
        title = e.title
        start = str(e.date)
        if e.time:
            start += 'T' + e.time.strftime('%H:%M:%S')
        items.append({
            'id': e.pk,
            'title': title,
            'start': start,
            'url': reverse('event-detail', args=[e.pk]),
            'category': e.category,
        })
    return JsonResponse(items, safe=False)
