from django.http import *
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from marketplace.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "base.html",{ 'is_home_page' : 1 })
        
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            error_dict={ 'login_error':1}
            return render_to_response('login.html',error_dict,context_instance=RequestContext(request))                   
    return render_to_response('login.html', context_instance=RequestContext(request))
    
def logout_user(request):
    logout(request) 
    return HttpResponseRedirect('/')       
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user_params = { "first_name":request.POST['first_name'],
                            "last_name":request.POST['last_name'],
                            "email":request.POST['email'], 
                          }
            is_seller = 0
            if request.POST.get('is_seller'):
                is_seller = 1            
            User.objects.filter(pk=new_user.id).update(**user_params)
            profile_obj,created = UserProfile.objects.get_or_create(user_id=new_user.id)                           
            profile_obj.is_seller = is_seller
            profile_obj.save()
            username = request.POST['username']
            password = request.POST['password1']              
            user = authenticate(username=username,password=password)
            login(request, user)              
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })    
