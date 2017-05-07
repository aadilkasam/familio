from django.contrib.auth.models import User
from .models import EditProfile, relationships
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


class editProfileForm(forms.ModelForm):

    class Meta:
        model = EditProfile
        fields = ('first_name', 'surname', 'gender', 'date_of_birth', 'condition',)

class familyMembersForm(forms.ModelForm):

    class Meta:
        model = relationships
        fields = ('name', 'sex', 'attribute', 'mother', 'father', 'husband', 'wife')
