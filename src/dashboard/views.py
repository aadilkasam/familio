from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerForm
from .forms import authenticateForm


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

class authenticateView2(View):
    form_class = authenticateForm
    template_name = 'dashboard/authenticate.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print('posting form')

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            print('form works fine')

            user = authenticate(username=username, password=password)

            auth_login(request, user)
            return redirect('dashboard:profile')


                # if user.is_active:
                #
                #     auth_login(request, user)
                #     return redirect('dashboard:profile')

        return render(request, self.template_name, {'form': form})
