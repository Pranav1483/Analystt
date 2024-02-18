from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from pytz import timezone
from django.conf import settings
from hashlib import sha256

zone = timezone(settings.TIME_ZONE)

def homepage(request):
    return render(request, 'todo_homepage.html')

def dashboard(request):
    if request.session.get('username', '') == '':
        return redirect('login')
    username = request.session.get('username', '')
    user_filter = User.objects.filter(username=username)
    if not user_filter.exists():
        request.session.clear()
        return redirect('login')
    user = user_filter.first()
    tasks_objects = Task.objects.filter(user=user)
    tasks = []
    for obj in tasks_objects:
        t = {}
        t['id'] = obj.id
        t['title'] = obj.title
        t['complete'] = obj.complete
        t['deadline'] = obj.deadline
        tasks.append(t)
    tasks.sort(key=lambda x: x['deadline'], reverse=True)
    return render(request, 'todo_dashboard.html', {'username': user.username, 'tasks': tasks})

def login(request):
    try:
        username, password = request.POST['username'], request.POST['password']
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.password = sha256(password.encode()).hexdigest()
            user.save()
            request.session['username'] = username
            return redirect('dashboard')
        else:
            if user.password == sha256(password.encode()).hexdigest():
                request.session['username'] = username
                return redirect('dashboard')
            else:
                request.session.clear()
                return redirect('login')
    except:
        request.session.clear()
        return redirect('login')
    
def addTaskPage(request):
    if request.session.get('username', '') == '':
        return redirect('login')
    username = request.session.get('username', '')
    user_filter = User.objects.filter(username=username)
    if not user_filter.exists():
        request.session.clear()
        return redirect('login')
    return render(request, 'todo_addtask.html')


def addTask(request):
    if request.session.get('username', '') == '':
        return redirect('login')
    username = request.session.get('username', '')
    user_filter = User.objects.filter(username=username)
    if not user_filter.exists():
        request.session.clear()
        return redirect('login')
    user = user_filter.first()
    try:
        task = Task(user=user, title=request.POST['task'], complete=False, deadline=zone.localize(datetime.strptime(request.POST['deadline'], "%Y-%m-%dT%H:%M")))
        task.save()
        return redirect('dashboard')
    except Exception as e:
        print(e)
        return redirect('addTaskPage')
    
def deleteTask(request, id):
    if request.session.get('username', '') == '':
        return redirect('login')
    username = request.session.get('username', '')
    user_filter = User.objects.filter(username=username)
    if not user_filter.exists():
        request.session.clear()
        return redirect('login')
    task = Task.objects.filter(id=id)
    if not task.exists():
        return redirect('dashboard')
    else:
        task.first().delete()
        return redirect('dashboard')

def updateTask(request, id):
    if request.session.get('username', '') == '':
        return redirect('login')
    username = request.session.get('username', '')
    user_filter = User.objects.filter(username=username)
    if not user_filter.exists():
        request.session.clear()
        return redirect('login')
    task = Task.objects.filter(id=id)
    if not task.exists():
        return redirect('dashboard')
    else:
        obj = task.first()
        obj.complete = not obj.complete
        obj.save()
        return redirect('dashboard')

def logout(request):
    request.session.clear()
    return redirect('login')
