from django.urls import path
from . import views

urlpatterns = [
    path('', views.bulletin_home, name='bulletin-home'),
    path('add/', views.add_announcement, name='bulletin-add'),
    path('edit/<int:pk>/', views.edit_announcement, name='bulletin-edit'),
]
