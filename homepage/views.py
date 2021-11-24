from django.shortcuts import redirect, render
from registration.models import user_profile

# Create your views here.
def home(request):
    return redirect('CV:home')
