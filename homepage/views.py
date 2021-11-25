from django.http import request
from django.shortcuts import redirect, render
from registration.models import user_profile

# Create your views here.
def home(request):
    
    if 'lang' not in request.session:
        #setting initial session value to en
        request.session['lang'] = 'en'
    
    return redirect('CV:about')

def change_language(request, pk):
    print('changing language !!' , pk , type(pk))
    if 'lang' not in request.session:
        #setting initial session value to en
        request.session['lang'] = 'en'
    else:
        if request.session['lang'] == 'en':
            request.session['lang'] = 'jp'
        else:
            request.session['lang'] = 'en'

    if pk == '1':    
        return redirect('CV:about')

    elif pk == '2':
        return redirect('CV:linktree')
    
    elif pk == '3':
        return redirect('CV:resume')

    elif pk == '4':
        return redirect('CV:projects')

    elif pk == '5':
        return redirect('CV:others')
    else:
        return redirect('homepage:home')
    
