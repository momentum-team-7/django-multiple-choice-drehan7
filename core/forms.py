from django import forms
from .models import User, Snippet

class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()
    class Meta:
        model = Snippet
        fields = ['title','author','code', 'language']
            
