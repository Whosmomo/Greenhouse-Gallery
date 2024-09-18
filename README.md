Web Deployment : https://pbp.cs.ui.ac.id/web/project/pradipta.wachyu/greenhousegallery

======================= TUGAS 2 =======================
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

======================= TUGAS 3 =======================
Pertanyaan - pertanyaan :
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
->kita memerluka data delivery untuk memastikan bahwa informasi yang dibutuhkan oleh komponen atau pengguna platform dapat dikirim secara lancar
dan akurat, data delivery juga berperan dalam keamanan data karena mencangkup metode enkripsi untuk melindungi data yang dikirim.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
-> menurut saya ada situasi dimana menggunakan salah satu format data lebih menguntungkan, saat menghadapi data yang lebih kompleks XML lebih baik
dibanding JSON karena mengandung skema namespace yang lebih kompleks. XML juga memiliki alat validasi yang kuat dan memiliki dokumentasi yang jelas.
Sementara itu JSON memiliki struktur yang lebih sederhana dibanding XML ini membuat JSON lebih unggul saat berurusan dengan API, ini juga mengapa 
JSON lebih populer dibanding XML karena kesederhanaan dan dukungan yang luas di berbagai platform.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
->is_valid() berfungsi untuk memeriksa apakah data yang dikirim melalui form valid atau tidak, ini memastikan bahwa data yang diterima sesuai dengan
aturan atau format yang diharapkan. Dengan method is_valid() kita dapat memeriksa semua field dalam form untuk validasi data, serta kita dapat 
mengendalikan alur program kita.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
->crsf_token diperlukan agar dapat melindungi aplikasi dari serangan CRSF(Cross-Site Request Forgery Token) dimana penyerang mecoba membuat
pengguna mengirim permintaan yang tidak sah ke server tanpa sepengetahuan pengguna. Jika kita tidak menambah crssf_token pada form Django yang kita buat maka penyerang dapat memanfaatkan authenticated session pada situs korban untuk megirimkan permintaan yang akan divalidasi oleh aplikasi sehingga penyerang dapat melakukan aksi pada akun user lain.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
->Untuk membuat input form pada aplikasi, saya membuat berkas forms.py dan membuat method yang menerima model seperti name dan description. Kemudian saya menambah method yang menerima parameter request untuk menampilkan data dalam bentuk xml, json dan data berdasarkan id. Terakhir saya membuat routing url dengan mengimport method yang saya buat dan menambah path URL ke dalam urlpatterns untuk mengakses method.

![postman json url](screenshot\postman_json.png)
![postman json by id url](screenshot\postman_json_id.png)
![postman xml url](screenshot\postman_xml.png")
![postman xml by id url](screenshot\postman_xml_id.png")