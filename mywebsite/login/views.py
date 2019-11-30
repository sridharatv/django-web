from django.shortcuts import render
from .forms import UserForm, CustomUserForm

# Imports for login and logout

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index (request):
    return render(request, 'login/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = CustomUserForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print("Got a valid request")
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture'  in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print("Form is INVALID")
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CustomUserForm()


    return render(request, 'login/register.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login:index'))
            else:
                return HttpResponse("Account is not Active")
        else:
            print("Unauthorized access! Someone tryed to login and failed")
            print("User name {}; Password {}".format(username,password))
            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'login/login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))

