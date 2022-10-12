# Assignment - Tugas 4

## Rafito Humam Abrar - 2106633626
## PBP E

*Klik untuk mengganti Readme Tugas 4, 5, dan 6: [Tugas 4](README.md), [Tugas 5](README.t5.md), [Tugas 6]("README - TWO.md")*

Berikut saya lampirkan link dari aplikasi yang berhasil di-*deploy* ke Heroku.

[LINK APLIKASI TUGAS 4](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 4 - todolist")

## Apa kegunaan `{% csrf_token %}` pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF Token merupakan sebuah potongan token random yang dibuat untuk mencegah serangan CSRF atau *Cross Site Request Forgery*. Potongan kode `{% csrf_token %}` akan men-*generate* token dari server dan akan melakukan *cross-checking* dari setiap request yang masuk dan hanya menjalankan yang memiliki token sesuai. Selain itu, tidak akan diekskusi untuk menjamin keamanan dari data *user*.

Jika tidak ada potongan kode tersebut di bawah elemen `<form>`, khususnya dalam metode POST, maka aplikasi akan me-*return* kode 403 yaitu kode untuk *Forbidden*, karena token tidak berhasil untuk di-*generate* maupun di verifikasi secara benar dengan status `*CSRF token missing*`. Karena itu, proses penyimpanan task akan bersifat gagal.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan *generator* seperti `{{ form.as_table }})?` Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Tentu saja bisa. Salah satu contohnya adalah HTML dari form yang digunakan untuk aplikasi ini. Form tersebut dibuat dengan menggunakan *method* POST, sehingga dibutuhkan inisiasi CSRF Token dengan kode seperti berikut:

```shell
...
 <form method="POST" >  
            {% csrf_token %}
            ...
```

Setelah itu, kita dapat menginisiasi tag `<table>` untuk membuat sebuah table yang digunakan untuk proses input form nantinya. Kemudian, kita tinggal mengkonstruksi isi dari tabel tersebut dengan potongan kode `<tr>` dan `<td>` serta tidak lupa untuk menginsiasi input dengan *type*, *name*, dan *value* yang sesuai.

Kemudian, untuk mendefinisikan jenis form, saya membuat *class* form yang disimpan dalam file `forms.py`. Isi dari file ini adalah `class TaskForm` yang menerima parameter ModelForm dari `django.forms`. Didalamnya terdapat `class Meta:` yang akan menerima model Task (berisi task-task user) dan jenis *field* yang akan diterima, yaitu `title` dan `description` berikut:

```shell
from django.forms import ModelForm
from todolist.models import Task

class TaskForm(ModelForm):
     class Meta:
         model = Task
         fields = ['title', 'description']
```

Nantinya, *class* ini yang nantinya akan dipanggil dalam views.py pada fungsi `create_task` yang akan mengvalidasi parameter `request` sebagai user yang sesuai dan nantinya direturn dan ditampilkan dalam bentuk html.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Salah satu contoh submisi data yang terjadi adalah di proses untuk membuat *task* baru. Ketika *user* melakukan klik pada tombol "POST" yang dimuat pada `create_task.html`, maka *input* yang diberikan oleh user akan segera divalidasi menggunakan fungsi `create_task` di `views.py`. Variabel `form` berisi `class TaskForm` yang diambil dari `forms.py` akan memastikan bahwa metode yang digunakan dalah POST. Kemudian, jika data berhasil divalidasi, maka data akan disimpan dengan perintah `form.save()` sesuai dengan logika yang developer inginkan. Dalam kasus ini, data disimpan sebagai models dengan *field* yang disesuaikan sebagai *title* dan *description* dari suatu *task*. Nantinya, data ini akan disimpan sebagai variabel `context` yang dapat dimunculkan dengan delivery ke *template* `todolist.html`.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas!

Pada awal mula, untuk membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya, kita hanya perlu mengetikkan *command* berikut di terminal:

```python
python manage.py startapp todolist
```

Setelah itu, folder `todolist` akan segera terbuat dan dapat dimodifikasi lebih lanjut.

Kedua, untuk menambahkan *path* atau *routing* untuk aplikasi `todolist` dapat dilakukan dengan mengisi *command* berikut di file `urls.py` yang terdapat pada lingkup ```prodject-django```:

```python
path('todolist/', include('todolist.urls'))
```

Ketiga, menambahkan *models* di file `models.py` dengan setiap *field* yang sesuai dengan konten yang diharapkan. Isi dari file `models.py` adalah sebagai berikut:

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
```

Hal tersebut dilakukan untuk menginisiasi berbagai models seperti *user*, *date*, *title*, dan *description* sesuai dengan konten `todolist` nantinya. Setelah itu, jangan lupa untuk melakukan migrasi skema model dengan mengetikkan `python manage.py makemigrations` dan `python manage.py migrate` di terminal.

Keempat, untuk menimplementasikan form *registrasi*, *login*, dan *logout*, serta tombol *create new task* perlu modifikasi dan penambahan dari file `views.py`, `urls.py`, `forms.py`, serta pembuatan template `.html` yaitu `login.html`, `new_task.html` serta `register.html`.

### views.py

```python
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
```
Pada `views.py`, diperlukan penambahan fungsi `register`, `login_user`, `logout_user` sesuai dengan instruksi pada Lab 03 beserta mekanisme untuk menerapkan restriksi serta *cookies* setiap *user*. Kemudian, untuk `create_task` dibuat untuk meng-*handle* serta validasi form pembuatan *task*, seperti berikut:

```python
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
```

Fungsi ini akan menerima parameter *request* dan akan melakukan validasi jika `class TaskForm` menggunakan metode POST, kemudian melanjutkan untuk validasi dari setiap data yang di-*pass* oleh form *task* tersebut. Form tersebut nantinya akan menjadi *models* dengan *fields* dari *title* dan *description*. Kemudian, fungsi tersebut juga menarik nilai nama *user* dan waktu ketika task dibuat dan disimpan pada model *user* serta *date*. Lalu akan dilakukan perintah *form.save()* yang akan menyimpan setiap *models* agar kemudian dijadikan sebuah *response* yang akan mengarahkan *models* tersebut untuk di-*render* sebagai *context* di fungsi `show_todolist`.

### urls.py

Pada file `urls.py`, perlu ditambahkan beberapa baris *path* di `urlpatterns` tersebut agar *routing* dari setiap fungsi dan aplikasi akan berjalan dengan sesuai.

```python
from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]
```

### forms.py

`forms.py` dibuat untuk menyimpan *class* *ModelForm* bernama `TaskForm` yang berfungsi untuk melakukan *updating* dari setiap *models* dan *field* yang sesuai untuk form `create_task`, dalam hal ini adalah dua jenis *field*, yaitu `title` dan `description`. Untuk implementasi kodenya daalah sebagai berikut:

```python
from django.forms import ModelForm
from todolist.models import Task

# Create the form class
class TaskForm(ModelForm):
     class Meta:
         model = Task
         fields = ['title', 'description']
```

### template files (.html)

Dalam implementasi *template* kali ini, dibutuhkan *template* `login.html` dan `register.html` sebagai *template* untuk halaman *login* dan *register* *user*. Kemudian, untuk isi dari `todolist.html` adalah sebagai berikut:

```python
{% extends 'base.html' %}

 {% block content %}
 <style>
  table, th, td {
  border: 1px solid rgb(0, 0, 0);
  }
  tr {background-color: rgba(0, 0, 0, 0.395);}

  body{
    color: rgb(255, 255, 255);
  }
</style>

  <h1>Tugas 4 Assignment PBP/PBD</h1>

  <h5>Name: {{username}}</h5>

  <button><a href="{% url 'todolist:create_task' %}">Create New Task</a></button>
  
  <table>
    <tr>
      <tr></tr>
      <th>Tanggal</th>
      <th>Judul Task</th>
      <th>Deskripsi</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for task in alltask %}
    <tr>
      <th>{{task.date}}</th>
      <th>{{task.title}}</th>
      <th>{{task.description}}</th>
    </tr>
    {% endfor %}
  </table>

  <h5>Sesi terakhir login: {{ last_login }}</h5>

  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

 {% endblock content %}
```

Hal yang perlu diperhatikan adalah menambahkan dua tombol yaitu *Create New Task* serta *Logout* dengan kode `<button><a href="{% url 'todolist:create_task' %}">Create New Task</a></button>` serta `<button><a href="{% url 'todolist:logout' %}">Logout</a></button>`. Kemudian, perlu disesuaikan setioap variabel agar dapat mengakses setiap *models* secara benar dan melakukan *printing* informasi ke pengguna secara benar dan jelas.

Adapun untuk `new_task.html` memiliki peran sebagai *template* halaman pengisian *task* baru, sehingga setiap *models* harus disesuaikan agar setiap *title* dan *description* dapat tersimpan dengan benar. Jangan lupa untuk membuat form dengan metode POST serta melakukan *generate* serta validasi CSRF token dengan kode `<form method="POST" >` dan `{% csrf_token %}` seperti berikut:

```python
{% extends 'base.html' %}

{% block meta %}
<title>Create Task</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    <h1>Create New Task</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                <tr>
                    <td>Title: </td>
                    <td>{{form.title}}</td>
                </tr>
                        
                <tr>
                    <td>Description: </td>
                    <td>{{form.description}}</td>
                </tr>
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="POST"/></td>  
                </tr>  
            </table>  
        </form>

</div>

{% endblock content %}
```

### Deployment ke Aplikasi Heroku

Setiap perubahan dari file - file yang disebutkan akan di-*tracking* dengan git menggunakan kode `git add .` Kemudian, file tersebut di-*commit* menggunakan potongan kode `git commit -m "{Masukkan pesan commit}"` dan pada akhirnya di-*push* ke repositori GitHub yang bersangkutan dengan kode `git push -u origin main`. Semua urutan ini dilakukan untuk melakukan *push* ke repositori GitHub, bukan untuk melakukan *deployment*.

Untuk melakukan *deployment* ke aplikasi Heroku, diperlukan untuk membuat aplikasi Heroku terlebih dahulu dan melakukan *assignment* API *key* ke variabel *secret* dari repositori GitHub. Hal ini dilakukan karna konfigurasi *deploy* di file `dpl.yml` menggunakan variabel rahasia yang perlu diatur pada pengaturan repositori dengan variabel `HEROKU_API_KEY` dan `HEROKU_APP_NAME`. Jika kedua variabel ini sudah terdefinisi secara baik, maka *deployment* akan berjalan secara mandiri dan terlaksana dengan baik.

Setelah *deployment* dilakukan, aplikasi katalog tersebut dapat diakses di link disini.

[LINK APLIKASI TUGAS 4](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 4 - Katalog")

Adapaun untuk test, saya telah membuat dua akun dummy dan telah membuat tiga task yang dapat diakses dengan *credentials* seperti berikut:

```shell
username: dummy1
password: rafitomanis234

username: dummy2
password: rafitomanis234
```

## Daftar Pustaka

Template ini dibuat berdasarkan [Repositori Template Lab PBP](https://github.com/pbp-fasilkom-ui/assignment-repository).
Beberapa materi didapat dari [Tutorial 3 PBP](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3), [HTML Code Library](https://www.quackit.com/html/codes/html_code_library.cfm), serta [Penjelasan ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/).
