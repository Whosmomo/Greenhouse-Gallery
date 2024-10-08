Web Deployment : https://pbp.cs.ui.ac.id/web/project/pradipta.wachyu/greenhousegallery

# TUGAS 2
## Pertanyaan - pertanyaan :

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

# TUGAS 3
## Pertanyaan - pertanyaan :
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

# TUGAS 4
## Pertanyaan - pertanyaan :
Apa perbedaan antara HttpResponseRedirect() dan redirect()?
->HttpResponseRedirect() dan redirect() sama-sama digunakan untuk mengarahkan pengguna ke url lain, namun HttpResponseRedirect() hanya dapat menerima URL string sedangkan redirect() dapat menerima URL string, nama URL, atau objek model. Ini membuat redirect() lebih fleksibel dalam penggunaan sedangkan HttpResponseRedirect() digunakan untuk pengalihan yang lebih spesifik berdasarkan URL.

Jelaskan cara kerja penghubungan model Product dengan User!
->Dengan ForeignKey kita dapat menautkan satu instance model ke satu user, ini dikarenakan ForeignKey memiliki hubungan many-to-one sehingga model Product pasti terasosiasikan dengan seorang User. 

Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
->authentication adalah proses verifikasi identitas pengguna, authorization adalah proses menentukan apakah pengguna yang terautentikasi memiliki izin untuk melakukan tindakan tertentu. Fungsi authenticate memverifikasi kredisensial pengguna, jika valid maka method akan mengembalikan objek pengguna. decorator @login_required dapat membatasi akses ke tampilan tertentu hanya untuk pengguna yang terautentikasi.

Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
->Setelah pengguna berhasil login pengguna diberi session ID yang di simpan dalam cookie di browser mereka, Django menggunakan session ID ini untuk menghubungkan permintaan pengguna dengan data sesi yang disimpan di server. Selain untuk sesi login cookies dapat digunakan untuk preferences pengguna seperti bahasa, tema, dll. Selain itu cookies dapat digunakan untuk mengumpulkan data aktivitas pengguna. Tidak semua cookies aman digunakan, cookies dapat disalahgunakan untuk membuat permintaan palsu atas nama pengguna yang telah login. Terdapat juga cookies yang tidak terenkripsi yang dapat diintersep oleh penyerang. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-> Saya menggunakan impor formulir bawaan UserCreationForm untuk membuat form regristrasi user, saya juga menggunakan import authenticate, login, logout, dan AuthenticationForm untuk melakukan autentikasi dan mengimplementasi fitur login dan logout, kemudian saya menggunakan ForeignKey untuk menghubungkan model Product dengan user agar aplikasi menampilkan model yang berbeda untuk masing-masing user. Kemudian pada server lokal saya membuat 2 akun melalui form regristrasi dan mendaftarkan 3 buah product untuk masing-masing akun. Terakhir saya mengimplementasi cookies dengan fungsi last_login dimana cookies yang dibuat oleh fungsi response.set_cookie('last_login', str(datetime.datetime.now())) akan ditambahkan pada respon yang dibuat menggunakan HttpResponseRedirect. 

# TUGAS 5
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
-> urutan prioritas : Inline style > ID selector > Classes > Element > Universal selector.
Specificity dihitung berdasarkan kombinasi nilai-nilai berikut: 
Inline style: Ditandai dengan 1 0 0 0 
ID selector: Ditandai dengan 0 1 0 0 
Class selector, attribute selector, pseudo-class: Ditandai dengan 0 0 1 0 
Element (tag) selector dan pseudo-element: Ditandai dengan 0 0 0 1 
Ketika beberapa selector berlaku untuk elemen yang sama, specificty ditentukan dengan menjumlahkan nilai masing-masing selector, dan aturan dengan specificity lebih tinggi akan diutamakan.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
->Responsive design penting dalam pengembangan aplikasi web karena memastikan tampilan dan pengalaman pengguna tetap optimal di berbagai perangkat, seperti smartphone, tablet, dan desktop. Dengan semakin banyaknya orang yang mengakses web dari perangkat mobile, desain responsif membantu aplikasi web beradaptasi dengan ukuran layar yang berbeda tanpa kehilangan fungsionalitas atau estetika. Ini meningkatkan pengalaman pengguna (user experience) dan membantu menjaga performa situs.
contoh aplikasi yang sudah menerapkan responsive design : Twitter, spotify
contoh aplikasi yang belum menerapkan responsive design : Situs Web Klasik yang Tidak Dioptimalkan: Beberapa situs web lama, misalnya situs web pemerintah atau sekolah yang jarang diperbarui, sering kali tidak mendukung desain responsif. Pada layar ponsel, elemen-elemen tampilan seperti teks atau gambar mungkin terlihat tidak proporsional, terlalu kecil, atau membutuhkan pengguliran horizontal yang mengganggu.

 Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
 ->Margin adalah ruang kosong di luar elemen, yang mengontrol jarak antara elemen dengan elemen lainnya.Margin tidak memiliki warna dan transparan. Border adalah garis yang mengelilingi elemen. Border membentuk tepi elemen dan bisa memiliki ketebalan, gaya, dan warna. Padding adalah ruang di dalam elemen, antara konten elemen dan border elemen. Padding menciptakan jarak antara konten dan tepi elemen (border).

 Jelaskan konsep flex box dan grid layout beserta kegunaannya!
 -> Flexbox adalah metode tata letak satu dimensi yang berguna untuk mendistribusikan ruang di antara elemen-elemen dalam satu baris atau satu kolom. Flexbox memungkinkan penyesuaian tata letak yang responsif dan fleksibel. Flex box berguna dalam mengatur elemen dalam satu dimensi dan cocok untuk tata letak sederhana seperti navigation bar, daftar produk, dll.
 CSS Grid Layout adalah sistem tata letak dua dimensi yang memberikan kontrol lebih besar dalam menyusun elemen-elemen baik secara horizontal maupun vertikal. Ini memungkinkan pembagian area konten menjadi baris dan kolom.

  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  -> untuk implementasi fitur edit product saya method untuk menyiapkan form dan mengambil entri product berdasarkan id serta melakukan perubahan apabila form valid dan di submit. Untuk delete product saya membuat method untuk mengambil entri product berdasarkan id dan menghapusnya menggunakan .delete(). Kemudian saya menggunakan tailwind dan styling css untuk kustomisasi agar web lebih menarik dan responsive untuk versi desktop dan juga mobile. 

# TUGAS 6
## Pertanyaan - pertanyaan :
Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
-> JavaScript memungkinkan pengembangan aplikasi web yang interaktif dan responsif dengan berjalan di sisi klien, mengurangi beban server dan mempercepat waktu respons. Dengan kemampuan untuk memanipulasi elemen HTML dan CSS secara dinamis, JavaScript menciptakan pengalaman pengguna yang lebih baik. Selain itu, dukungan luas dari berbagai framework dan integrasi API menjadikannya alat penting untuk membangun aplikasi web yang cepat, fungsional, dan kompatibel lintas platform.

Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
->Fungsi await dalam penggunaan fetch() adalah untuk menunggu hingga operasi fetch() selesai dan mendapatkan hasilnya sebelum melanjutkan eksekusi kode berikutnya. fetch() mengembalikan Promise, dan await memastikan bahwa nilai dari promise tersebut (misalnya, respons HTTP) diperoleh sebelum melakukan tindakan lebih lanjut. Jika await tidak digunakan, hasil dari fetch() tidak akan langsung tersedia, dan kode berikutnya mungkin gagal karena mencoba mengakses hasil yang belum siap.

Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
-> Decorator csrf_exempt digunakan pada view di Django untuk menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) pada view tertentu, seperti ketika menangani AJAX POST request. Dalam konteks ini, kita menggunakan csrf_exempt karena permintaan AJAX sering kali tidak membawa token CSRF, yang diperlukan untuk validasi oleh Django. Jika token CSRF tidak ada atau tidak valid, Django akan menolak permintaan POST dan mengembalikan error 403 (Forbidden).

Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
-> Pembersihan input di backend memastikan bahwa data yang diterima oleh server selalu aman dan sesuai standar, sehingga menghindari ancaman keamanan serta memastikan integritas dan konsistensi sistem.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
-> Saya mengimplementasi AJAX GET dan POST dengan menambah fungsi baru di views.py yang berfungsi untuk menambah product tanpa harus refresh halaman web. Saya mengubah fungsi show_json dan show_xml untuk melakukan pengambilan data product yang terkait dengan user dengan cara memfilter berdasarkan user yang sedang login. Saya menambah mengaitkan tombol untuk men-**_trigger_** modal untuk menambah product baru secara AJAX. Terakhir saya membuat path untuk menghubungkan form yang sudah dibuat.




