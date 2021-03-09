from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import User, Snippet, Profile
from .forms import SnippetForm, ProfileForm
import os
import pyperclip
from functools import reduce

# Create your views here.

def index(request):

    users = User.objects.all()
    profiles = Profile.objects.all()

    return render(request, 'index.html', {'users': users})

@login_required
def feed(request):
    users = User.objects.all()
    profiles = Profile.objects.all() 

    current_user = User.objects.get(username = request.user.username)
    if current_user.username not in [profile.user.username for profile in profiles]:
        new_profile = Profile.objects.create(
            user=current_user,
            
        )
        new_profile.save()

    return render(request, 'public_feed.html', {'users': users, 'profiles': profiles})

@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    count = len(user.snippets.all())
    if count > 0:
        totalCopies = reduce((lambda x, y: x + y),[snip.copies for snip in user.snippets.all()])

    else:
        totalCopies = 0

    return render(request, 'user_profile.html', {'user': user, 'profile':profile, 'count':count, 'copies' : totalCopies})

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
  
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        data = {'deleted':'True'}
    else:
        data = {'deleted': 'False'}

    return JsonResponse(data)

@login_required
def search_results(request, pk):
    search_input = request.GET['query']
    code_results = Snippet.objects.filter(author=request.user, code__icontains=search_input)
    lang_results = Snippet.objects.filter(author=request.user,language__icontains=search_input)
    final_results = code_results | lang_results
    return render(request, 'search_results.html', {'final_results':final_results, 'search_input': search_input})

@login_required
def update_pic(request, pk):
    
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            user.picture = form.cleaned_data['picture']
            user.save()
            print("FORM VALID !!!")
            return HttpResponseRedirect(f'/user/{pk}/profile/')
        
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'update_pic.html', {"form": form})

@login_required
def copy_snippet(request,snippetPK):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        snippet = Snippet.objects.get(pk=snippetPK)
        snippet.copies+=1
        new_snippet = Snippet.objects.create(
            title=snippet.title, 
            author=request.user, 
            code=snippet.code, 
            language=snippet.language, 
            copies=0
        )
        new_snippet.save()
        snippet.save()
        pyperclip.copy(snippet.code)
        data = {
            "copied" : "True"
        }
    else:
        data = {
            'copied': 'False'
        }

    return JsonResponse(data)
 