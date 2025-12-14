from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Subscription, CATEGORY_CHOICES
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

def events_list(request):
    events = Event.objects.order_by('date', 'time')
    user_subscriptions = []
    if request.user.is_authenticated:
        user_subscriptions = Subscription.objects.filter(user=request.user).values_list('category', flat=True)

    return render(request, 'events/calendar.html', {
        'events': events,
        'categories': CATEGORY_CHOICES,
        'user_subscriptions': user_subscriptions,
    })

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
    if request.method == 'POST':
        subscription, created = Subscription.objects.get_or_create(user=request.user, category=category)
        if created:
            # Send an email notification
            send_mail(
                subject=f'You subscribed to {category} events!',
                message=f'Hi {request.user.username},\n\nYou have successfully subscribed to {category} events. You will now receive email notifications for new events in this category.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )
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
        start = str(e.date)
        if e.time:
            start += 'T' + e.time.strftime('%H:%M:%S')
        items.append({
            'id': e.pk,
            'title': e.title,
            'start': start,
            'url': reverse('event-detail', args=[e.pk]),
            'lat': getattr(e, 'lat', None),
            'lng': getattr(e, 'lng', None),
            'category': e.category
        })
    return JsonResponse(items, safe=False)
