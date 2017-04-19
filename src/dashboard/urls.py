"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'dashboard'

urlpatterns = [

    url(r'^add_family_members', views.add_family_members, name= 'add_family_members'),
    url(r'^family_members', views.family_members, name= 'family_members'),
    url(r'^example_tree', views.example_tree, name= 'example_tree'),
    url(r'^view_tree', views.view_tree, name= 'view_tree'),
    url(r'^edit/$', views.edit_profile, name = 'edit_profile'),
    url(r'^authenticate/$', views.authenticateView.as_view()),
    url(r'^register/$', views.registerView.as_view()),
    url(r'^logout/$', views.logoutUser),
    url(r'^$', views.dashboard, name = 'profile')

]
