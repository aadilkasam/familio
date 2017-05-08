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
from .forms import registerForm, authenticateForm, familyMembersForm
from models import sampleTree, relationships
from django.contrib.auth.models import User
import json
from django.shortcuts import render_to_response
from django.core import serializers


# Create your views here.

# goto main profile page if user is logged in
def dashboard(request):

    if not request.user.is_authenticated():
        print('not logged in');
        return HttpResponseRedirect('/profile/authenticate')

    return render(request, 'dashboard/profile.html', {})

# log in form
def login(request):
    form_class = registerForm
    template_name = 'dashboard/registration_form.html'
    return render(request, self.template_name, {'form': form})

# log out user from website
def logoutUser(request):
    logout(request)
    return redirect('/')


# register class for website
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

# authenticate if user has signed up
class authenticateView(View):
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

# view family members
@login_required
def family_members(request):

    myLocalID = request.user.id
    data = relationships.objects.filter(UserID=myLocalID)
    print(request.user.id)
    print(data)
    return render(request, 'dashboard/family_members.html', {'data': data })

# add family members to database
def add_family_members(request):

    if request.method=='POST':
        form = familyMembersForm(request.POST)
        # save field values
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

# edit family members
def member_update(request, id):
    myLocalID = request.user.id
    data = relationships.objects.filter(UserID=myLocalID)
    instance = get_object_or_404(relationships, key=id)
    form = familyMembersForm(request.POST or None, instance=instance)
    if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          return redirect('dashboard:family_members')
    return render(request, 'dashboard/update_family_members.html', {'form': form, 'data': data})

# delete family members from database
def member_delete(request, id):
    instance = get_object_or_404(relationships, key=id)
    instance.delete()
    return redirect('dashboard:family_members')

# view tree with pre loaded data
def example_tree(request):
    return render(request, 'dashboard/example_tree.html')

# view sample tree with hardcoded data
def view_sample_tree(request):

    data = sampleTree.objects.all()
    return render(request, 'dashboard/view_sample_tree.html', {'data': data })

# view tree of data inputted by the user
def view_tree(request):

    myLocalID = request.user.id
    data = relationships.objects.filter(UserID=myLocalID)
    print(data)
    return render(request, 'dashboard/view_tree.html', {'data': data })
