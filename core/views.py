from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User, Snippet

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

@login_required
def feed(request):
    users = User.objects.all()
    return render(request, 'public_feed.html', {'users': users})

@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_profile.html', {'user': user})