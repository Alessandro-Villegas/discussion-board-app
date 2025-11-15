from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit-post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete-post'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/upvote/', views.upvote_post, name='upvote-post'),
    path('post/<int:pk>/downvote/', views.downvote_post, name='downvote-post'),
]
