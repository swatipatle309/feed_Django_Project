from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post_message/', views.post_message, name='post_message'),
    path('post_comment/<int:message_id>/', views.post_comment, name='post_comment'),
    path('like_message/<int:message_id>/', views.like_message, name='like_message'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
]

