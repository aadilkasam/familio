from django.shortcuts import render

# Create your views here.
def landing_home(request):
    return render(request, 'landing/index.html', {})
