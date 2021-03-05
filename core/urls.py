from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/feed/', views.feed, name='feed'),
    path('user/<int:pk>/profile/', views.user_profile, name='user_profile'),
    path('user/<int:pk>/profile/add/', views.add_snippet, name='add_snippet'),
    path('user/<int:pk>/profile/edit/<int:id>/', views.edit_snippet, name='edit_snippet'),
]
