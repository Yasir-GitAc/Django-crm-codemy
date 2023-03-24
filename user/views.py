from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import SignUpForm, TaskForm
from . models import Task
# Create your views here.

@login_required(login_url='login')
def home(request):
  user = request.user
  tasks = user.task_set.all().order_by('-created_at')
  tasks_incompleted = user.task_set.filter(completed=False)
  return render(request,'home.html', {'user':user, 'tasks':tasks, 'tasks_incompleted':tasks_incompleted})

def view_uncompleted(request):
  user = request.user
  tasks_uncompleted = user.task_set.filter(completed=False)
  
  return render(request,'view_uncompleted.html', {'user':user, 'tasks_uncompleted':tasks_uncompleted})


def login_user(request):
  if request.method == 'POST':

    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request,user)
      messages.success(request,"welcome back!")
      return redirect('home')
    else:
      messages.success(request,"Error,please try again")
      return redirect('login')
  else:
    return render(request, 'login.html', {})


def logout_user(request):
  logout(request)
  messages.success(request,"logout successful")
  return redirect('login')


def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, 'Registration Successful')
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html',{'form':form})
  
  return render(request, 'register.html',{'form':form})


@login_required(login_url='login')
def new_task(request):
  user = User.objects.get(pk=request.user.id)
  form = TaskForm()
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      # user = form.cleaned_data['user']
      userstask = form.save(commit=False)
      userstask.user = user
      userstask.save()
      print(request.POST)
      print(user)
      return redirect('home')
  else:
    form = TaskForm()
  return render(request,'new_task.html', {'form':form})


def update_task(request,pk):
  task = Task.objects.get(pk=pk)
  form = TaskForm(request.POST or None, instance=task)
  if form.is_valid():
    form.save()
    messages.success(request,'task has been updated')
    return redirect('home')
  return render(request,'update_task.html',{'form':form})

def delete_task(request,pk):
  task = Task.objects.get(pk=pk)
  task.delete()
  messages.success(request,'task deleted')
  return redirect('home')

