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

### `<ins>` atau `<u>`
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

Untuk mengimplementasikan *checklist* di atas, kita perlu melakukan kostumisasi HTML dan CSS setiap halaman, serta menggunakan *CSS Framework*. Untuk mengimplementasi *source code* dari *CSS Framework*, dalam hal ini adalah *Bootstrap*, perlu ditambahkan potongan cource code *Bootstrap* di HTML utama (`index.html` maupun `base.html`) seperti berikut:

```shell
<head>
    ...
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    ...
</head>
```

```shell
<body>
    ...
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    ...
</body>
```

Hal ini akan berguna untuk menambahkan elemen-elemen HTML yang sudah terdapat di *source code* Bootstrap agar bisa dipakai di dalam halaman HTML.

Kemudian, saya melakukan visualisasi dari setiap halaman `todolist` agar sesuai dengan selera saya. Pada tugas 5, saya menggunakan *color scheme* berwarna oranye dan hitam. Adapun untuk menyusun tema seperti berikut, perlu mendefinisikan beberapa *Internal CSS* di dalam tag `<style></style>` dan perubahan di kode HTML itu sendiri. Salah satu contohnya adalah `Internal CSS` dalam file `login.html`:

```shell
<style type="text/css">
      Html, body {
        height:100%;
      }
      .grandParentContaniner {
        display:table; height:100%; margin: 0 auto;
      }
      .parentContainer {
        display:table-cell; vertical-align:middle;
      } 
      body {
        background-image: url("https://i.pinimg.com/originals/38/51/8c/38518cc76d1965753247e4d35f82037a.jpg");
      }
      .submit {
        border-radius: 3px;
        box-sizing: border-box;
        color: rgb(0, 0, 0);
        cursor: pointer;
        font-size: 15px;
        height: 40px;
        margin-top: 10px;
        margin-left: 10px;
        text-align: center;
        width: 50%;
      }
      .submit:hover {
        box-shadow: 0 0.5em 0.3em -0.2em var(--hover);
        transform: translateY(-0.15em);
      }
      .container {
        padding: 25px;
        border-radius: 5px;   
        background-color: rgb(255, 140, 0);
        opacity: 100%;  
      }
      h1 {
        color: white;
        text-shadow: 2px 2px rgb(0, 0, 0);
        text-align: center;
      }
</style>
```

Adapun kode tersebut digunakan untuk menampilkan sebuah *wrapper container* untuk *form login*, menampilkan elemen-elemen di tengah halaman, serta kostumisasi setiap teks agar sesuai dengan kesesuaian dari tema website. Hal ini terus dilakukan untuk setiap halaman HTML (`login.html`, `register.html`, `new_task.hml`, dan `todolist.html`) agar setiap halaman dituntut untuk kesesuaian tema dari satu sama lain.

Hal yang berbeda adalah pada `todolist.html`, karena terdapat tambahan implementasi untuk menambahkan elemen `cards` seperti berikut:

CSS

```shell
    ...
    .card {
      background-color: #ff8c00;
      text-align: center;
      box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
      transition: 0.3s;
      border-radius: 5px;
      margin-bottom: 15px;
    }
    .card:hover {
      transform: translateY(3px);
    }
    .container {
      padding: 20px 10px;
    }
    ...
```

Untuk HTMLnya, perlu ditambahkan `<div>` dari class tersebut untuk *for-loop* yang didefinisikan untuk printing kegiatan, seperti berikut:

```shell
    ...
    <br>
    .{% for task in alltask %}
    <div class="card">
      <div class="container">
        <h4><b>{{task.title}}</b></h4>
        <p>{{task.description}}</p>
        <p>{{task.date}}</p>
      </div>
    </div>
    {% endfor %}
    <br>
    ...
```

Untuk membuat keempat halaman menjadi *responsive*, setiap kostumisasi CSS harus memiliki atribut yang menyesuaikan dengan setiap *resolusi* dari device yang berbeda. Untuk *Bootstrap*, perlu didefinisikan potongan kode tersebut agar elemen yang dihasilkan bersifat responsif:

```shell
    <head>
        ...
        <meta name="viewport" content="width=device-width, initial-scale=1">
        ...
    </head>
```

### Deployment ke Aplikasi Heroku

Setiap perubahan dari file - file yang disebutkan akan di-*tracking* dengan git menggunakan kode `git add .` Kemudian, file tersebut di-*commit* menggunakan potongan kode `git commit -m "{Masukkan pesan commit}"` dan pada akhirnya di-*push* ke repositori GitHub yang bersangkutan dengan kode `git push -u origin main`. Semua urutan ini dilakukan untuk melakukan *push* ke repositori GitHub, bukan untuk melakukan *deployment*.

Untuk melakukan *deployment* ke aplikasi Heroku, diperlukan untuk membuat aplikasi Heroku terlebih dahulu dan melakukan *assignment* API *key* ke variabel *secret* dari repositori GitHub. Hal ini dilakukan karna konfigurasi *deploy* di file `dpl.yml` menggunakan variabel rahasia yang perlu diatur pada pengaturan repositori dengan variabel `HEROKU_API_KEY` dan `HEROKU_APP_NAME`. Jika kedua variabel ini sudah terdefinisi secara baik, maka *deployment* akan berjalan secara mandiri dan terlaksana dengan baik.

Setelah *deployment* dilakukan, aplikasi katalog tersebut dapat diakses di link disini.

[LINK APLIKASI TUGAS 5](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 5 - todolist")

## Daftar Pustaka

Template ini dibuat berdasarkan [Repositori Template Lab PBP](https://github.com/pbp-fasilkom-ui/assignment-repository).
Beberapa materi didapat dari [Tutorial 4 PBP](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-4), [Pembelajaran HTML](https://www.youtube.com/watch?v=tVBuw-RkUU4&ab_channel=BelajarCoding), [Pembelajaran CSS](https://www.youtube.com/watch?v=r9xO1ZafoW4&t=2876s&ab_channel=BelajarCoding), [Membuat Vertical Align Elemen](https://blog.e-zest.com/tutorial-how-to-vertical-center-align-a-login-form-or-container-div/), serta [Membuat Cards](https://www.w3schools.com/howto/howto_css_cards.asp).
