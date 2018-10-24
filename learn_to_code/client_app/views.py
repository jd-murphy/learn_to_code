from django.shortcuts import render
from client_app.forms import ClientLoginForm
from client_app.models import Lesson, ClientProfileInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'client_app/index.html')


def client_registration(request):
    registered = False
    if request.method == "POST":
        user_form = ClientLoginForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = ClientLoginForm()
    return render(request, 'client_app/register.html', 
                context={ 'registered': registered, 'user_form': user_form })


def client_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('client_app:client_code'))
            else:
                return HttpResponseRedirect(reverse('client_registration'))
        else:
            print('Login failed.')
            print(f"Username: {username}  Password: {password}")
            return HttpResponse('Invalid login credentials!')
    else:
        return render(request, 'client_app/login.html')


@login_required
def client_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def code(request):
    lesson_number = 1
    current_lesson = f"lessons/lesson_{lesson_number}.html"
    context = {'lesson': current_lesson }
    return render(request, 'client_app/code.html',  context=context)


@login_required
def lessons(request):
    return render(request, 'client_app/lessons.html')