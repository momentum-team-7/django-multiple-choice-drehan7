from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>/', views.user_profile, name='user_profile'),
]
