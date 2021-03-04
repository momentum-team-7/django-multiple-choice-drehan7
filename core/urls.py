from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>/profile/', views.user_profile, name='user_profile'),
]
