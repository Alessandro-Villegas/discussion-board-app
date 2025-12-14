from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_list, name='emergency-list'),
    path('add/', views.add_emergency, name='add-emergency'),
    path('edit/<int:pk>/', views.edit_emergency, name='edit-emergency'),
    path('delete/<int:pk>/', views.delete_emergency, name='delete-emergency'),
]