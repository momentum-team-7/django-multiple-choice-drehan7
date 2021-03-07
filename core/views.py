from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import User, Snippet, Profile
from .forms import SnippetForm, ProfileForm

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

@login_required
def add_snippet(request, pk):
    if request.user.pk != pk:
        return render(request, 'error.html')

    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, initial={'author':user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/feed/')

    else:
        form = SnippetForm()
    return render(request, 'add_snippet.html', {'form':form})

@login_required
def edit_snippet(request, pk, id):
    snippet = get_object_or_404(Snippet, pk=id)
    if request.user.pk != snippet.author.pk:
        return render(request, 'error.html')
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/user/{pk}/profile/')
    else:
        form = SnippetForm(instance=snippet)
    
    return render(request, 'edit_snippet.html', {'form':form, 'snippet':snippet})

@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.user.pk != snippet.author.pk:
        return render(request, 'error.html')
    snippet.delete()
    return HttpResponseRedirect(f'/user/{snippet.author.pk}/profile/')

@login_required
def search_results(request, pk):
    search_input = request.GET['query']
    results = Snippet.objects.filter(code__icontains=search_input)
    return render(request, 'search_results.html', {'results':results, 'search_input': search_input})

@login_required
def update_pic(request, pk):
    
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.picture = request.FILES['picture']
            form.save()
            return HttpResponseRedirect(f'/user/{pk}/profile/')
    else:
        form = ProfileForm(instance=user)
   
    return render(request, 'update_pic.html', {"form": form})