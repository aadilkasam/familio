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
        fields = ('name', 'sex', 'DOB' , 'attribute', 'smoker', 'mother', 'father', 'husband', 'wife')
        help_texts = {
            'attribute': 'Enter the conditions with a single space between each condition. (A B C D S) S = Deceased',
            'DOB': 'Enter your date of birth - DD/MM/YYYY',
            'smoker': 'Tick the box if true',
            'mother': 'Enter the key (number) of your mother',
            'father': 'Enter the key (number) of your father',
            'husband': 'Enter the key (number) of your husband',
            'wife': 'Enter the key (number) of your wife',
        }
