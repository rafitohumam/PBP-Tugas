import datetime
from urllib import request
from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
    'alltask': Task.objects.filter(user = request.user),
    'username': request.user,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
    'alltask': Task.objects.filter(user = request.user),
    'username': request.user,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data = BarangWishlist.objects(user = request.user).filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.instance.date = datetime.date.today()
        form.save()
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        return response

    context = {'form': form}
    return render(request, "new_task.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Akun telah berhasil dibuat!')
        return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
