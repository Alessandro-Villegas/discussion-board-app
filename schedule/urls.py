from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='schedule-home'),
    path('add/', views.add_activity, name='add-activity'),
    path('<int:pk>/edit/', views.edit_activity, name='edit-activity'),
    path('<int:pk>/delete/', views.delete_activity, name='delete-activity'),
]
