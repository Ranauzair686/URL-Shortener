from django import forms

class URLForm(forms.Form):
    long_url = forms.URLField(label='Enter your URL', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your URL here...'
    }))
