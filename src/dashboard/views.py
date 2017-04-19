from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerForm, authenticateForm, editProfileForm, familyMembersForm
from models import sampleTree, relationships

import json

from django.shortcuts import render_to_response
from django.core import serializers


# Create your views here.
def dashboard(request):

    if not request.user.is_authenticated():
        print('not logged in');
        # return render(request,'dashboard/login.html', {})
        return HttpResponseRedirect('/profile/authenticate')


    return render(request, 'dashboard/profile.html', {})


def login(request):
    form_class = registerForm
    template_name = 'dashboard/registration_form.html'

    # display blank form
    # def get(self, request):
    #     form = self.form_class(None)
    #     return render(request, self.template_name, {'form': form})

    return render(request, self.template_name, {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('/')


class registerView(View):
    form_class = registerForm
    template_name = 'dashboard/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            print('form works fine')


            user = form.save(commit=False)

            # clean (normalised) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    auth_login(request, user)
                    return redirect('dashboard:profile')

        return render(request, self.template_name, {'form': form})

class authenticateView(View):
    # print('im in authenticate view')
    form_class = authenticateForm
    template_name = 'dashboard/authenticate.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user.is_active:

            auth_login(request, user)
            return redirect('dashboard:profile')

        return render(request, self.template_name, {'form': form})

def edit_profile(request):
    form = editProfileForm()
    return render(request, 'dashboard/edit_profile.html', {'form': form})


def example_tree(request):

    # data = serializers.serialize('json', sampleTree.objects.all(), fields=('relations'))
    return render(request, 'dashboard/example_tree.html')

def family_members(request):

    # data = serializers.serialize('json', sampleTree.objects.all(), fields=('relations'))
    data = relationships.objects.all()
    print(data)
    return render(request, 'dashboard/family_members.html', {'data': data })

def add_family_members(request):

    # data = serializers.serialize('json', sampleTree.objects.all(), fields=('relations'))
    if request.method=='POST':
        form = familyMembersForm(request.POST)
        if form.is_valid():
            member=form.save(commit=False)
            member.name=request.POST.get('name')
            member.sex=request.POST.get('sex')
            member.attribute=request.POST.get('attribute')

            member.save()
            return redirect('dashboard:family_members')

    else:
        form = familyMembersForm()
    return render(request, 'dashboard/add_family_members.html', {'form': form})



def view_tree(request):

    # data = serializers.serialize('json', sampleTree.objects.all(), fields=('relations'))
    data = sampleTree.objects.all()
    return render(request, 'dashboard/view_tree.html', {'data': data })
