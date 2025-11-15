from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list, name='events-list'),
    path('json/', views.events_json, name='events-json'),
    path('add/', views.add_event, name='events-add'),
    path('<int:pk>/', views.event_detail, name='event-detail'),
    path('subscribe/<str:category>/', views.subscribe_category, name='subscribe-category'),
    path('unsubscribe/<str:category>/', views.unsubscribe_category, name='unsubscribe-category'),
]
