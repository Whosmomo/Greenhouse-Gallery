Web Deployment :

Pertanyaan - pertanyaan :
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
->setelah mendapatkan ide tentang tema aplikasi, saya membuat sebuah direktori kosong dengan nama Greenhouse-Gallery. Setelah mengaktifkan
virtual environment saya menjalankan perintah untuk membuat aplikasi main. Setelah menambah file urls.py saya menggunakan fungsi show_main
agar aplikasi dapat ditampilkan. Saya mengubah berkas models.py yang ada di direktori main untuk menambah atribut yang saya inginkan.
Saya membuat direktori templates dan mengisiya dengan file main.html yang berisi nama aplikasi dan nama dan kelas saya. Kemudian saya membuat fungsi
show_main pada views.py untuk menampilkan template html yang sudah saya buat. Terakhir saya membuat routing pada urls.py dengan menambah rute url
path('', include('main.urls')), dalam variable urlpatterns. Terakhir saya melakukan git add commit dan push serta melakukan deployment ke situs PWS.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
->ketika client melakukan request ke suatu URL tertentu, urls.py mencocokan URL request dengan view yang tepat dimana views.py 
berinteraksi dengan models.py untunk mengambil data dari database. views.py akan mengirim data ke berkas html untuk dirender dan dikembalikan
sebagai respons ke client

Client -> Django urls -> views <-> models <-> database
  ^                         |        
  |                         v             
  | _ _ _ _ _ _ _ _ _ _ template

Jelaskan fungsi git dalam pengembangan perangkat lunak!
->git adalah sistem kontrol versi yang berfungsi untuk mengelola dan melacak perubahan pada kode sumber. Pengguna dapat menyimpan berbagai
versi kode dalam repositori terpusat, git memungkinkan beberapa pengguna untuk bekerja sama pada projek yang sama dengan adanya beberapa branch
untuk menngerjakan suatu fitur tanpa menggangu kode utama.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
->Penggunaan arsitektur MVC (Model-View-Controller) yang memudahkan kita dalam memahami struktur umum pengembangan perangkat lunak.
Django mempunyai banyak fitur yang memungkinkan seseorang untuk membuat prototipe dengan ccepat sehingga seseorang dapat melihat hasil dari
apa yang mereka pelajari.

Mengapa model pada Django disebut sebagai ORM?
->karena Django menghubungkan objek python secara langsung ke tabel database tanpa harus menulis SQL secara langsung.