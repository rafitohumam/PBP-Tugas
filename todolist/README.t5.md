# Assignment - Tugas 5

## Rafito Humam Abrar - 2106633626
## PBP E

*Klik untuk mengganti Readme Tugas 4 dan 5: [Tugas 4](README.md), [Tugas 5](README.t5.md)*

Berikut saya lampirkan link dari aplikasi yang berhasil di-*deploy* ke Heroku.

[LINK APLIKASI TUGAS 5](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 5 - todolist")

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

CSS atau *Cascading Style Sheets* merupakan sebuah bahasa yang berfungsi menentukan format visual suatu website berdasar *markup language* seperti HTML maupun XML agar memiliki tampilan yang lebih memanjakan mata pengguna. Adapun cara implementasi dari CSS terbagi menjadi tiga jenis, yaitu *Inline CSS*, *Internal CSS*, serta *External CSS*.

Perbedaan dari ketiga bahasa ini adalah letak penempatan, cara pemanggilan, sifat pemanggilan, serta urutan prioritas dari CSS itu sendiri.

### Inline CSS
*Inline CSS* memiliki penempatan di dalam elemen HTML itu sendiri sebagai sebuah atribut. Misalkan jika kita ingin menulis sebuah teks berjenis h1, maka potongan kodenya seperti berikut:

```shell
<h1>Selamat datang di repositori Rafito Humam</h1>
```

Namun, jika kita ingin memodifikasi visual dari tulisan tersebut dengan warna oranye, maka kita dapat mengimplementasikan *Inline CSS* sebagai atribut dari h1, sebagai berikut:

```shell
<h1 style="color: orange;">Selamat datang di repositori Rafito Humam</h1>
```

Kelebihan dari metode ini adalah implementasinya cepat, praktis, dan selalu mendapat prioritas pertama dalam inisiasi. Namun pastinya terdapat kelemahan jika elemen yang ingin dikostumisasi berjumlah banyak, sehingga kita harus mengkostumisasi setiap visual dari masing-masing elemen.

### Internal CSS
*Internal CSS* memiliki implementasi di dalam elemen `<style>` di bawah lingkup `<head>` dari sebuah HTML. Bentuk CSS seperti ini bersifat lebih universal, karena modifikasi visual berkemungkinan untuk diterapkan ke semua elemen, tidak hanya elemen individual seperti *Inline CSS* saja. Dalam *inline css*, dilakukan Inisiasi selector CSS. Misalkan jika kit ingin melakukan perubahan yang sama seperti *Inline CSS*, maka potongan kodenya adalah sebagai berikut

```shell
<head>
    ...
    <style type="text/css">
            h1 {
                background-color: orange;
            }
        </style>
        ...
</head>
```

Kelebihan dari metode ini adalah inisiasi visual tidak perlu dilakukan satu-satu per elemen dalam satu halaman,namun jika terdapat banyak halaman HTML akan sulit untuk menyelaraskan setiap halaman dengan baik. Serta dengan banyak potongan kode CSS di setiap awal HTML tidak terlihat rapih.

### External CSS
Seperti namanya, *External CSS* merupakan implementasi CSS dengan mengambil kode visualisasi dari file external dengan format `.css`, bukan berasal dari file HTML itu sendiri. Pada file `.css`, kita perlu mendefinisikan setiap *selector* dan elemen visualisasinya seperti pada *Internal CSS*, misalkan seperti ini:

```shell
            h1 {
                background-color: orange;
            }
```

Namun pada file HTML yang ingin kita kostumisasi perlu ditambahkan potongan kode untuk mengambil elemen visualisasi dari file `.css` tersebut, dengan:

```shell
<head>
    ...
    <link rel="stylesheet" type="text/css" href="external.css">
    ...
</head>
```

Kelebihan dari metode ini adalah inisiasi visual tidak perlu dilakukan satu-satu per halaman. Setiap adanya perubahan segi visual, maka akan berubah juga untuk setiap halaman yang melakukan referensi ke file `.css` tersebut sehingga lebih efisien, cepat, dan konsisten. Namun, metode ini memiliki kelemahan jika file `.css` tersebut terjadi masalah atau belum bisa ter-*load* dengan baik, maka semua halaman HTML tidak akan terpampang dengan sempurna pula.

Dalam kasus ini, dimisalkan file tersebut adalah `external.css`.

*Internal CSS* memiliki implementasi di dalam elemen `<style>` di bawah lingkup `<head>` dari sebuah HTML. Bentuk CSS seperti ini bersifat lebih universal, karena modifikasi visual berkemungkinan untuk diterapkan ke semua elemen, tidak hanya elemen individual seperti *Inline CSS* saja. Dalam *inline css*, dilakukan Inisiasi selector CSS. Misalkan jika kit ingin melakukan perubahan yang sama seperti *Inline CSS*, maka potongan kodenya adalah sebagai berikut

```shell
<head>
    ...
    <style type="text/css">
            h1 {
                background-color: orange;
            }
        </style>
        ...
</head>
```

##  Jelaskan tag HTML5 yang kamu ketahui

HTML merupakan sebuah file representasi halaman yang dipenuhi oleh *tags*. Maka dari itu, jumlah *tags* sangatlah banyak sekali. Adapun beberapa jenis *tag* yang saya ketahui adalah:

### `<head>` dan `<body>`
Kedua *tag* ini adalah *tag* yang sangat penting bagi file HTML. *tag* `<head>`merupakan sebuah kontainer atau tempat penyimpanan dari semua elemen *head* yang diperlukan. Beberapa contohnya adalah `<title>`, `<meta>`, bahkan `<style>` yang mewakili CSS dalam lingkup *tag* `<head>`.

Selain itu, terdapat juga `<body>`, yang merupakan bagian utama yang menampung isi dari dokumen halaman tersebut. Hal ini termasuk dengan setiap teks, gambar, *link*, tabel, *list*, bahkan *iframe*. Semua elemen halaman yang ingin ditampilkan sebagai sebuah data / dokumen akan disisipkan di bawah *tag* `body` ini.

Seperti biasa, tidak lupa untuk menutup setiap *tag* terebut dengan `</head>` maupun `</body>`.

### `<h1>` hingga `<h6>`
*Tag* ini digunakan untuk menulis sebuah teks sebagai *heading*. Sebagai sebuah *heading*, tentunya ukurannya relatif lebih besar dibandingkan sebuah paragraf. Maka dari itu, disediakan berbagai macam ukuran *font* dari *tags* tersebut yang diurutkan dari terbesar (`<h1>`) hingga yang terkecil (`<h6>`) .

### `<strong>` atau `<b>`
*Tag* `<strong>` atau `<b>` biasanya digunakan dalam sebuah tag paragraf (`<p>`) untuk memunculkan efek *bold* atau huruf tebal dalam sebuah teks.

### `<ins>` atau `<u>```
*Tag* `<em>` atau `<i>` biasanya digunakan dalam sebuah tag paragraf (`<p>`) untuk memunculkan efek *italic* atau huruf miring dalam sebuah teks.

### `<em>` atau `<i>`
*Tag* `<ins>` atau `<u>` biasanya digunakan dalam sebuah tag paragraf (`<p>`) untuk memunculkan efek *underline* atau garis bawah dalam sebuah teks.

### `<hr>`
*Tag* `<hr>` biasanya digunakan untuk menambahkan garis horizontal dalam sebuah halaman. *Tag* ini dapat digunakan tanpa tag penutup `</hr>`.

### `<br>`
*Tag* `<br>` biasanya digunakan untuk menambahkan suatu *line break* atau jeda kosong dalam sebuah teks, layaknya perintah `println("\n")`. *Tag* ini dapat digunakan tanpa tag penutup `</br>`

### `<p>`
Berbeda dengan *heading*, *tag* ini digunakan untuk menulis sebuah teks sebagai paragraf. Layaknya sebuah paragraf, *tag* `<p>` digunakan untuk menulis banyak teks yang dimunculkan dalam halaman HTML. Maka dari itu, ukuran *default font* dari *tag* `<p>` relatif lebih kecil dibandingkan heading dengan *tag* `<h1>` hingga `<h6>`.

### `<table>`, `<tr>`, `<th>`, dan `<td>`
*Tag* `<table>`, `<tr>`, dan `<td>` dan serangkaian tag lainnya (`<tbody>`, `<thead>`, dll.) digunakan untuk membuat sebuah tabel dalam HTML. `<table>` dan `</table>` digunakan untuk inisiasi elemen-elemen tabel, sedangkan `<tr>` digunakan untuk menginisiasi setiap row tabel, `<th>` digunakan untuk *heading* setiap tabel, dan `<td>` untuk menginisasi konten atau data dari tabel.
 
Selain berbagai *tag* di atas, terdapat beberapa *tag* lain yang mewakili elemen-elemen format HTML, seperti `<div>`, `<span>`, `<ul>`, `<ol>`, dan lainnya.

## Jelaskan tipe-tipe selector yang kamu ketahui!
Sesuai dengan namanya, *selector* merupakan cara untuk memilih implementasi dari kode CSS untuk melakukan viasualisasi pada halaman HTML. Biasanya, *selector* tersebut didefinisikan di dalam tag `<style>` dan dapat dipanggil pada setiap elemen HTML. Terdapat beberapa tipe *selector* yang umum diketahui, yaitu:

### Element Selector
*Element Selector* mewakili pemilihan kostumisasi HTML untuk setiap jenis elemen. Misalkan, jika kita ingin melakukan visualisasi terhadap heading dengan jenis `<h1>`, maka digunakan element selector seperti berikut:

```shell
...
<style type="text/css">
		h1 {
			color: orange;
		}
	</style>
    ...
```

Jika hal ini diaplikasi, maka setiap heading dengan jenis `<h1>` akan divisualisasi sesuai dengan persyaratan *element selector* di atas dengan warna oranye.

### Class Selector
*Class Selector* mewakili pemilihan kostumisasi HTML dengan membuat sebuah *class*. *Class* ini dapat berupa kata apapun dengan diawali sebuah titik `.`. *Class* ini kemudian akan dipanggil di setiap inisiasi elemen. Misalkan, saya akan membuat sebuah kostumisasi *class selector* dengan nama *class* orange seperti berikut: 

```shell
...
<style type="text/css">
	.orange {
		color: orange;
	}
</style>
 ...
```

Kemudian kostumisasi ini dapat diterapkan ke elemen manapun yang memanggilnya. Sebagai contoh:

```shell
...
<body>
    <h1 class="orange">Selamat datang di repositori Rafito Humam</h1>
    <p class="orange">Selamat datang di repositori Rafito Humam</p>
</body>
    ...
```

Jika hal ini diaplikasi, maka untuk kedua elemen di atas akan divisualisasi sesuai dengan persyaratan *class selector* di atas dengan warna oranye, walaupun antar kedua elemen tersebut memiliki jenis yang berbeda. *Class selector* juga dapat dipanggil berkali-kali untuk semua jenis elemen.

### ID Selector
*ID Selector* mewakili pemilihan kostumisasi HTML dengan membuat sebuah *ID*. *ID* ini dapat berupa kata maupun angka apapun dengan diawali sebuah tanda pagar `#`. *Class* ini kemudian akan dipanggil ke hanya tepat satu inisiasi elemen. Misalkan, saya akan membuat sebuah kostumisasi *ID selector* dengan nama *class* orange seperti berikut: 

```shell
...
<style type="text/css">
	#orange {
		color: orange;
	}
</style>
 ...
```

Kemudian kostumisasi ini dapat diterapkan hanya tepat satu elemen yang memanggilnya.

```shell
...
<body>
    <h1 id="orange">Selamat datang di repositori Rafito Humam</h1>
</body>
    ...
```

Jika hal ini diaplikasi, maka untuk tepat satu di atas akan divisualisasi sesuai dengan persyaratan *ID selector* di atas dengan warna oranye.

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
