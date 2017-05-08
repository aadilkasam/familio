from django.contrib.auth.models import User
from .models import relationships
from django import forms
from datetime import date

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
        fields = ('name', 'sex', 'DOB' , 'attribute', 'mother', 'father', 'husband', 'wife')
        help_texts = {
            'attribute': 'Enter the conditions with a single space between each condition. (A B C D S) S = Deceased',
            'DOB': 'Enter your date of birth - DD/MM/YYYY',
        }

class relationshipsForm(forms.ModelForm):

    class Meta:
        model = relationships
        fields = ('name', 'mother', 'father', 'husband', 'wife')
