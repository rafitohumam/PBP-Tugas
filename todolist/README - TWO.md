# Assignment - Tugas 6

## Rafito Humam Abrar - 2106633626
## PBP E

Berikut saya lampirkan link dari aplikasi yang berhasil di-*deploy* ke Heroku.

[LINK APLIKASI TUGAS 6](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 5 - todolist")

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

### Asynchronus Programming
*Programming* yang bersifat *asynchronous* memiliki arsitektur *non-blocking*, artinya program tersebut tidak akan melakukan pemblokiran untuk penambahan eksekusi atau proses baru ketika suatu proses sedang dijalankan.

### Synchronus Programming
*Programming* yang bersifat *synchronous* memiliki arsitektur *blocking*, artinya program tersebut akan melakukan pemblokiran penambahan eksekusi atau proses baru ketika suatu proses sedang dijalankan.

Perbedaan antar keduanya adalah *asynchronous programming* bersifat *multi-thread*, sehingga dapat melakukan operasi yang banyak dalam waktu yang bersamaan. *Asynchronous programming* dapat mengirimkan banyak *request* ke server dalam waktu bersamaan. Hal ini berbeda dengan sifat *synchronus programming* yaitu *single-thread* yang akan menunggu satu *request* untuk selesai terlebih dahulu baru kemudian dapat mengirimkan *request* yang lainnnya.

##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!

Sesuai dengan namanya, *event-driven programming* merupakan sebuah paradigma yang menyatakan bahwa setiap *response* yang diberikan oleh program dipicu oleh oleh suatu *event*, perilaku, atau aksi yang dilakukan antara user dan server. *Event - event* ini dapat berupa sebuah klik tombol, hover dari elemen, bahkan koordinat dari kursor *mouse*.

Pada Tugas 6, implementasi AJAX GET maupun POST yang secara asinkronus dilakukan di *background* setelah sebuah *button* ditekan merupakan salah satu contoh *event-driven programming*.

## Jelaskan penerapan asynchronous programming pada AJAX.

Pada dasarnya, AJAX atau *Asynchronous JavaScript and XML* memang sebuah teknik untuk mengimplementasikan asynchronous progrmamming ke dalam sebuah website untuk meningkatkan kecepatan respons dan memberikan *user experience* yang baik.

Salah satu bukti adanya *asynchronous programming* pada AJAX adalah *browser* sebagai pengakses tidak perlu melakukan *blocking* atau *suspend* dari *request-request* baru yang perlu ditangani. Sehingga, ketika sebuah fungsi berbasis AJAX dijalankan ketika di-*trigger* oleh sebuah *event*, maka *browser* tidak perlu melakukan *refresh* dan berjalan seperti biasa.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

### Implementasi file

1. Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX,
2. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON,
3. Membuat path /todolist/json yang mengarah ke view yang baru dibuat,
4. Lakukan pengambilan task menggunakan AJAX GET,
5. Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task,
6. Membuat view baru untuk menambahkan task baru ke dalam database,
7. Membuat path /todolist/add yang mengarah ke view yang baru kamu buat,
8. Menghubungkan form yang telah dibuat di dalam modal ke path /todolist/add,
9. Melakukan modal setelah penambahan task telah berhasil dilakukan,
10. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.

### Deployment ke Aplikasi Heroku

Setiap perubahan dari file - file yang disebutkan akan di-*tracking* dengan git menggunakan kode `git add .` Kemudian, file tersebut di-*commit* menggunakan potongan kode `git commit -m "{Masukkan pesan commit}"` dan pada akhirnya di-*push* ke repositori GitHub yang bersangkutan dengan kode `git push -u origin main`. Semua urutan ini dilakukan untuk melakukan *push* ke repositori GitHub, bukan untuk melakukan *deployment*.

Untuk melakukan *deployment* ke aplikasi Heroku, diperlukan untuk membuat aplikasi Heroku terlebih dahulu dan melakukan *assignment* API *key* ke variabel *secret* dari repositori GitHub. Hal ini dilakukan karna konfigurasi *deploy* di file `dpl.yml` menggunakan variabel rahasia yang perlu diatur pada pengaturan repositori dengan variabel `HEROKU_API_KEY` dan `HEROKU_APP_NAME`. Jika kedua variabel ini sudah terdefinisi secara baik, maka *deployment* akan berjalan secara mandiri dan terlaksana dengan baik.

Setelah *deployment* dilakukan, aplikasi katalog tersebut dapat diakses di link disini.

[LINK APLIKASI TUGAS 6](https://tugas3-rafitohumam.herokuapp.com/todolist/ "App Heroku Tugas 4 - Katalog")

## Daftar Pustaka

Template ini dibuat berdasarkan [Repositori Template Lab PBP](https://github.com/pbp-fasilkom-ui/assignment-repository).
Beberapa materi didapat dari [Tutorial 3 PBP](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3), [Event-Driven Programming](https://aiven.io/blog/introduction-to-event-based-programming), serta [Penjelasan AJAX](https://www.youtube.com/watch?v=rJesac0_Ftw&ab_channel=LearnWebCode).
