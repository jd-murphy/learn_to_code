from django.shortcuts import render
from client_app.forms import ClientLoginForm
from client_app.models import Lesson, ClientProfileInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
import json

# Create your views here.
def index(request):
    return render(request, 'client_app/index.html')


def client_registration(request):
    registered = False
    if request.method == "POST":
        user_form = ClientLoginForm(data=request.POST)
        profile = ClientProfileInfo()
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile.user = user
            profile.current_lesson = 1
            profile.completed_lessons = ''
            profile.save()
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
            return render(request, 'client_app/login.html', { 'error': 'Unsuccessful login attempt.' })
    else:
        return render(request, 'client_app/login.html')


@login_required
def client_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def code(request, lesson_number=1):
    current_lesson = int(request.user.clientprofileinfo.current_lesson)
    if lesson_number == 1:
        lesson_number = current_lesson
    try:
        lesson_info = Lesson.objects.get(pk=lesson_number)
    except LessonDoesNotExist:
        raise Http404("That lesson does not exist.")
    last_lesson = Lesson.objects.all().exclude(name="Not set").last()
    context = {'lesson': f"lessons/lesson_{lesson_number}.html", 'lesson_number': lesson_number, 'last_lesson': last_lesson.number }
    return render(request, 'client_app/code.html',  context=context)


@login_required
def lessons(request):
    completed_lessons = request.user.clientprofileinfo.completed_lessons
    lessons = Lesson.objects.all().exclude(name="Not set")
    if completed_lessons:
        completed_lessons = [int(i) for i in completed_lessons.split(',') if i]
    context = { 'lessons': lessons, 'completed_lessons': completed_lessons }
    return render(request, 'client_app/lessons.html', context=context)


@login_required
def reset(request):
    client_info = ClientProfileInfo.objects.get(user=request.user)
    client_info.completed_lessons = ""
    client_info.save()
    lessons = Lesson.objects.all().exclude(name="Not set")
    context = { 'lessons': lessons, 'completed_lessons': '' }
    return render(request, 'client_app/lessons.html', context=context)


@login_required
def complete_lesson(request):
    if request.method == "POST":
        lesson_number = request.POST.get('lesson_number')
    client_info = ClientProfileInfo.objects.get(user=request.user)
    client_info.completed_lessons += lesson_number + ","
    client_info.save()
    return HttpResponse(json.dumps({'success': 'Lesson marked as complete.'}), content_type="application/json")