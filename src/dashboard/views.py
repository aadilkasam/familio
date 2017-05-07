from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerForm, authenticateForm, editProfileForm, familyMembersForm
from models import sampleTree, relationships
from django.contrib.auth.models import User

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

@login_required
def family_members(request):

    # data = serializers.serialize('json', sampleTree.objects.all(), fields=('relations'))
    # data = relationships.objects.all()
    # myUserID = builtindjangounction to tell you what is is
    myLocalID = request.user.id
    data = relationships.objects.filter(UserID=myLocalID)
    print(request.user.id)
    # data = relationships.objects.filter(UserID__exact=1)
    print(data)
    return render(request, 'dashboard/family_members.html', {'data': data })

def add_family_members(request):

    if request.method=='POST':
        form = familyMembersForm(request.POST)
        if form.is_valid():
            member=form.save(commit=False)
            member.name=request.POST.get('name')
            member.sex=request.POST.get('sex')
            member.attribute=request.POST.get('attribute')
            member.UserID = request.user.id
            member.save()
            return redirect('dashboard:family_members')

    else:
        form = familyMembersForm()
    return render(request, 'dashboard/add_family_members.html', {'form': form})

def member_update(request, id):
    instance = get_object_or_404(relationships, key=id)
    form = familyMembersForm(request.POST or None, instance=instance)
    if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          return redirect('dashboard:family_members')
    return render(request, 'dashboard/update_family_members.html', {'form': form})

def member_delete(request, id):
    instance = get_object_or_404(relationships, key=id)
    instance.delete()
    return redirect('dashboard:family_members')


def view_sample_tree(request):

    data = sampleTree.objects.all()
    return render(request, 'dashboard/view_sample_tree.html', {'data': data })

def view_tree(request):

    myLocalID = request.user.id
    data = relationships.objects.filter(UserID=myLocalID).filter(key=3)
    print(data)
    return render(request, 'dashboard/view_tree.html', {'data': data })
