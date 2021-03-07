from django import forms
from .models import User, Snippet, Profile

class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()
    class Meta:
        model = Snippet
        fields = ['title','author','code', 'language']
            
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['user'].widget = forms.HiddenInput()
    class Meta:
        model = Profile
        fields = ['user', 'picture']