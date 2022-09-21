# Assignment - Tugas 3

## Rafito Humam Abrar - 2106633626
## PBP E

Berikut saya lampirkan link dari aplikasi yang berhasil di-*deploy* ke Heroku.

[LINK APLIKASI TUGAS 2](https://tugas2-rafitohumam.herokuapp.com/katalog/ "App Heroku Tugas 2 - Katalog")

## Cara Kerja Model, View, Template dari Django 

![alt text](baganreadme.jpg "Bagan Tugas 2")

Bagan di atas merupakan penggambaran implementasi dari struktur MVT (Model-View-Template) dari Django, khususnya pada Tugas 2. Pada awalnya, *user* sebagai *client* dari server Django akan melakukan sebuah permintaan yang ditangkap oleh `urls.py`. Kemudian, `urls.py` akan meneruskan permintaan tersebut kepada `views.py` dengan serangkaian fungsi yang didefinisikan oleh *developer* di dalam `views.py`. Sesuai dengan permintaan dan jalannya program, `views.py` akan melakukan pengambilan data berupa *query* ke `models.py` dan dikembalikan langsung ke `views.py`. Setelah permintaan tersebut berhasil dilaksanakan, maka program tersebut akan memetakan data tersebut ke sebuah *template*, dalam kasus ini diwakilkan oleh `katalog.html`, dan pada akhirnya dikembalikan ke *user* sebagai sebuah respons yang sesuai.

## Implementasi Poin 1 Hingga 4

Sesuai dari *template* soal Tugas 2 yang diberikan, terdapat empat poin yang dititikberatkan untuk mempersiapkan aplikasi hingga melakukan *deployment*, yaitu:

1. Membuat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pada awal mula, perlu dilakukan *cloning template* repositori dari *source code* tugas lab yang diberikan di GitHub ke sebuah repositori baru. Kemudian, *clone* repositori tersebut ke *local disk* sehingga dapat diakses secara lokal. Jika dilihat, sudah terdapat aplikasi lokal yang dibuat di terminal bernama katalog.

### views.py

Pertama, lakukan penyuntingan pada file `views.py` untuk melakukan pengambilan data dari `models.py` dan dipetakan ke *template* dalam file HTML.

```python
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    return render(request, "katalog.html", context)

data_barang_katalog = CatalogItem.objects.all()

context = {
    'list_barang': data_barang_katalog,
    'nama': 'Rafito Humam',
    'npm' : '2106633626'
}
```

Pada file `views.py` ini ditambahkan beberapa *line*, yaitu:
1. ```python
   from katalog.models import CatalogItem
   ```
*Line* ini dibuat untuk mengambil data dari `models.py`.

2. ```python 
   def show_katalog(request):
      return render(request, "katalog.html", context)

   context = {
    'list_barang': data_barang_katalog,
    'nama': 'Rafito Humam',
    'npm' : '2106633626'
   }
   ```
*Line* ini dibuat untuk mendefinisikan fungsi show_katalog dengan parameter `(request)` untuk melakukan *return* data dari database `models.py` dan di-*render* ke file *template* yaitu `katalog.html`. Data yang di-*render* berada pada variabel `context`, dimana berisi sebuah list barang katalog yang telah diimport dengan variabel `list_barang` dari `models.py` dan informasi nama serta NPM.

### urls.py

Untuk melakukan *routing* dari fungsi yang terdapat `views.py` tersebut, perlu dilakukan konfigurasi dari `urls.py` yang dalam bentuk final memiliki isi sebagai berikut:

`urls.py` pada folder `katalog`
```python
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

Pada file ini ditambahkan beberapa *line*, yaitu:
1. ```python
   from katalog.views import show_katalog
   ```
*Line* ini dibuat untuk memanggil fungsi `show_katalog` yang telah didefinisikan di `views.py`.

2. ```python
   app_name = 'katalog'

   urlpatterns = [
    path('', show_katalog, name='show_katalog'),
   ]
   ```
*Line* ini dibuat untuk mendefenisikan nama aplikasi di variabel `app_name` dengan nama katalog, serta mendaftarkan fungsi `show_katalog` di bawah variabel urlpatterns untuk mengarahkan *urls* ke fungsi yang tepat.

### models.py

Kemudian, ada file `models.py` yang berfungsi untuk mendefinisikan setiap *database* berupa variabel-variabel yang berada pada file `initial_catalog_data.json` dalam sebuah class bernama `CatalogItem`.

```python
from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
```

### katalog.html (template)

Finalisasi terakhir dilakukan dengan menambahkan *loop* ke file `katalog.html` seperti berikut:

```shell
<h1>Tugas 2 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{npm}}</p>

  <table>
    <tr>
      <tr></tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for barang in list_barang %}
        <tr>
            <th>{{barang.item_name}}</th>
            <th>{{barang.item_price}}</th>
            <th>{{barang.item_stock}}</th>
            <th>{{barang.rating}}</th>
            <th>{{barang.description}}</th>
            <th>{{barang.item_url}}</th>
        </tr>
  {% endfor %}
  </table>
  ```

  Loop yang ditambahkan tersebut berfungsi untuk menampung variabel-variabel katalog yang telah didefinisikan pada `views.py` serta data mengenai nama, harga, stok, rating, deskripsi, dan url setiap iterasi barang yang ditemukan di *range loop* `list_barang`. Kemudian, file `katalog.html` tersebut digunakan untuk menampilan informasi ke user.

### Deployment ke Aplikasi Heroku

Setiap perubahan dari file - file yang disebutkan akan di-*tracking* dengan git menggunakan kode `git add .` Kemudian, file tersebut di-*commit* menggunakan potongan kode `git commit -m "{Masukkan pesan commit}"` dan pada akhirnya di-*push* ke repositori GitHub yang bersangkutan dengan kode `git push -u origin main`. Semua urutan ini dilakukan untuk melakukan *push* ke repositori GitHub, bukan untuk melakukan *deployment*.

Untuk melakukan *deployment* ke aplikasi Heroku, diperlukan untuk membuat aplikasi Heroku terlebih dahulu dan melakukan *assignment* API *key* ke variabel *secret* dari repositori GitHub. Hal ini dilakukan karna konfigurasi *deploy* di file `dpl.yml` menggunakan variabel rahasia yang perlu diatur pada pengaturan repositori dengan variabel `HEROKU_API_KEY` dan `HEROKU_APP_NAME`. Jika kedua variabel ini sudah terdefinisi secara baik, maka *deployment* akan berjalan secara mandiri dan terlaksana dengan baik.

Setelah *deployment* dilakukan, aplikasi katalog tersebut dapat diakses di link disini.

[LINK APLIKASI TUGAS 2](https://tugas2-rafitohumam.herokuapp.com/katalog/ "App Heroku Tugas 2 - Katalog")

## Menggunakan Virtual Environment 

*Virtual environment* merupakan sebuah lingkungan *virtual* yang secara sengaja dibuat untuk menampung setiap pengembangan aplikasi python agar memiliki dependensi yang terpisah dari pengembangan-pengembangan yang lainnya. Hal ini berarti setiap *virtual environment* memiliki *requirements* atau persyaratannya masing-masing dalam berjalannya pengembangan. Mengembangkan suatu aplikasi python menggunakan sebuah lingkungan *virtual* akan mencegah adanya konflik yang terjadi karna irisan dari perbedaan konfigurasi, versi, maupun prasyarat pengembangan.

Walaupun sebenarnya sebuah aplikasi python dapat tetap dikembangkan di luar *virtual environment*, namun risiko konflik yang dapat terjadi antar pengembangan akan sangat tinggi. Tentu ini tidak sebanding dengan hanya membuat sebuah lingkungan *virtual* secara *bespoke* agar setiap aplikasi memiliki dependensi untuk dikembangkan secara aman dan tanpa konflik.

## Daftar Pustaka

Template ini dibuat berdasarkan [Repositori Template Lab PBP](https://github.com/pbp-fasilkom-ui/assignment-repository).
Beberapa materi didapat dari [Tutorial 1 PBP](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1) dan [Penjelasan Virtual Environment](https://towardsdatascience.com/why-you-should-use-a-virtual-environment-for-every-python-project-c17dab3b0fd0).