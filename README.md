<a name="readme-top"></a>
<h1 align="center">MyFood</h1>
<!-- TABLE OF CONTENTS -->
Daftar Isi
  <ol>
    <li><a href="#penjelasan-aplikasi">Penjelasan Aplikasi</a></li>
    <li><a href="#cara-menjalankan-aplikasi">Cara Menjalankan Aplikasi</a></li>
    <li>
      <a href="#daftar-modul">Daftar Modul</a>
      <ul>
        <li><a href="#modul-menu">Modul Menu</a></li>
      </ul>
      <ul>
        <li><a href="#modul-produk">Modul Produk</a></li>
      </ul>
      <ul>
        <li><a href="#modul-keranjang">Modul Keranjang</a></li>
      </ul>
    </li>
    <li>
      <a href="#daftar-tabel-basis-data">Daftar Tabel Basis Data</a>
      <ul>
        <li><a href="#tabel-data-menu-restoran">Tabel Data Menu Restoran</a></li>
      </ul>
      <ul>
        <li><a href="#tabel-data-pesanan-customer">Tabel Data Pesanan Customer</a></li>
      </ul>
    </li>
  </ol>

<!-- Penjelasan Aplikasi -->
## Penjelasan Aplikasi

**MyFood**

MyFood merupakan aplikasi pemesanan makanan di restoran yang bertujuan untuk membantu customer yang hendak melakukan pemesanan makanan melalui dekstop app yang tersedia pada restoran. Dengan adanya aplikasi ini, customer akan dimudahkan dalam melihat daftar menu, harga, dan dapat memesan makanan dan minuman sendiri melalui fitur keranjang dan checkout. Makanan yang telah dipesan customer otomatis masuk ke database milik restoran sehingga mempermudah koki dalam menyiapkan menu makanan.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Cara Menjalankan Aplikasi -->
## Cara Menjalankan Aplikasi

**Prerequisites**
1. Mengunduh file [DataRestoran.sql](https://github.com/salimashockbgt/TubesRPL/tree/master/src/db) yang tersedia pada folder src/db
2. Membuat database yang bernama DataRestoran pada postgreSQL, lalu mengimport file DataRestoran.sql pada database DataRestoran
3. Mengubah pengaturan server postgreSQL menjadi sebagai berikut:
          
          user="postgres",
          password="123",
          host="127.0.0.1",
          port=5432
4. Membuka folder src pada master branch lalu run program melalui file Main.py

Saat akan menjalankan program, lakukan instalasi pycoporg2 pada terminal.
  ```sh
  pip install psycopg2-binary
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Daftar Modul -->
## Daftar Modul
MyFood memiliki 3 modul terimplementasi yang telah dirancangkan pada dokumen perancangan perangkat lunak, yaitu modul menu, modul produk, dan modul keranjang

### Modul Menu
Mencakup DisplayMenuUI

         Verawati Esteria S. Simatupang - 18220002
         Salimatussholati Az Zahra - 18220054
         Christopher Jie - 18220052     
         
![170767](https://user-images.githubusercontent.com/88304323/204701841-89823cf4-2fa1-4109-a923-539d77290083.jpg)
<p align="center">Tampilan Menu</p>

![170768](https://user-images.githubusercontent.com/88304323/204701908-146cecd9-c2f8-4376-98a2-3c10e8722a15.jpg)
<p align="center">Tampilan Search Menu</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Modul Produk
Mencakup TambahProduk, MenuGUI1, MenuGUI2, MenuGUI3, MenuGUI4, MenuGUI5, dan MenuGUI6

         Agnes Tamara - 18220010
         
![menu1](https://user-images.githubusercontent.com/88304323/204703674-8bbe6db1-9339-460a-a6c2-09d3ea667b5d.jpg)
<p align="center">Tampilan Menu 1</p>

![menu2](https://user-images.githubusercontent.com/88304323/204703680-ac10f58f-d151-490d-a7cb-7ecee7672060.jpg)
<p align="center">Tampilan Menu 2</p>

![menu3](https://user-images.githubusercontent.com/88304323/204703686-be7f7792-7f5e-4cc7-8cbf-d90ccab54e12.jpg)
<p align="center">Tampilan Menu 3</p>

![menu4](https://user-images.githubusercontent.com/88304323/204703691-0f55e5c2-36c1-4590-8904-5959918bf7fe.jpg)
<p align="center">Tampilan Menu 4</p>

![menu5](https://user-images.githubusercontent.com/88304323/204703657-942dae15-4955-46b2-91d0-b21c9cea5a50.jpg)
<p align="center">Tampilan Menu 5</p>

![menu6](https://user-images.githubusercontent.com/88304323/204703662-acc628f4-c72f-4d09-a3c5-7a860701bfa1.jpg)
<p align="center">Tampilan Menu 6</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Modul Keranjang

Mencakup DisplayKeranjangUI dan DisplayStrukGUI 

         Muhammad Rayfasa Candra - 18220076
         Michel Vito Adinugroho - 18220066
         
![keranjang](https://user-images.githubusercontent.com/88304323/204703670-abdc8226-9592-44c8-b3ac-22d8a36d7a1e.jpg)
<p align="center">Tampilan Keranjang</p>

![checkout](https://user-images.githubusercontent.com/88304323/204703667-0f5badf4-8370-4a64-9f17-2849508641de.jpg)
<p align="center">Tampilan Checkout</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Penanggung Jawab Fitur

Verawati Esteria S. Simatupang - 18220002

         1. Tampilan Halaman Utama (Main)
         2. Menghapus Daftar Menu di Keranjang pada database (DeleteMenu)
         3. Menambah Produk (TambahProduk)

Agnes Tamara - 18220010

         1. Tampilan Daftar Menu GUI (DisplayMenuUI)
         2. Tampilan Halaman Setiap Produk (MenuGUI1, MenuGUI2, MenuGUI3, MenuGUI4, MenuGUI5, MenuGUI6)

Christopher Jie - 18220052

         1. Database datamenurestoran dan datapesanancustomer 
         2. Tampilan Daftar Menu Restoran dari Database (DisplayMenuUI)
         3. Tampilan Daftar Menu Restoran GUI (DisplayMenuUI)
         4. Fitur tambah/kurang barang (DisplayHalamanProduk)
         5. Fitur total dan subtotal (Checkout)
         6. Fitur hapus per item dan ubah kuantitas per item (DisplayHalamanProduk)
         7. Add notes (DisplayKeranjang) (parsial saja karena backendnya sudah di luar sistem)

Salimatussholati Az Zahra - 18220054

         1. Fitur Pencarian Menu (DisplayMenuUI)

Michel Vito Adinugroho - 18220066

         1. Tampilan Daftar Menu GUI (DisplayMenuUI)
         2. Tampilan CheckOut GUI (DisplayStrukGUI)
         3. Fitur total dan subtotal (Checkout)

Muhammad Rayfasa Candra - 18220076

         1. Tampilan Keranjang (DisplayKeranjangUI)

*diluar pembagian fitur, kami menerapkan colaboration working dalam menyelesaikan antar fungsi dan modul dengan kontribusi yang tidak bisa dituliskan satu per satu*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Daftar Tabel Basis Data -->
## Daftar Tabel Basis Data

*Daftar Tabel Basisdata :*
### Tabel Data Menu Restoran

```
datamenurestoran(id_barang, nama_barang, deskripsi_barang, harga_barang)
```
         
<img width="800" alt="DataMenuRestoran" src="https://user-images.githubusercontent.com/88304323/204720674-cdd61b3c-a805-4bc2-9ceb-f0db76905fa7.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tabel Data Pesanan Customer

```
datapesanancustomer(id_barang(foreign key), jumlah_barang, nama_barang, total_harga)
```
         
<img width="550" alt="DataPesananCustomer" src="https://user-images.githubusercontent.com/88304323/204721254-8baece73-509f-4b5f-a8d0-a07754c4cc29.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

