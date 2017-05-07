from django.contrib.auth.models import User
from .models import relationships
from django import forms

class registerForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class authenticateForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class familyMembersForm(forms.ModelForm):

    class Meta:
        model = relationships
        fields = ('name', 'sex', 'attribute', 'mother', 'father', 'husband', 'wife')
        help_texts = {
            'attribute': 'Enter the conditions with a single space between each condition. (A B C D S) S = Deceased',
        }

class relationshipsForm(forms.ModelForm):

    class Meta:
        model = relationships
        fields = ('name', 'mother', 'father', 'husband', 'wife')
