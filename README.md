**MyFood**

MyFood merupakan aplikasi pemesanan makanan di restoran yang bertujuan untuk membantu customer yang hendak melakukan pemesanan makanan melalui dekstop app yang tersedia pada restoran. Dengan adanya aplikasi ini, customer akan dimudahkan dalam melihat daftar menu, harga, dan dapat memesan makanan dan minuman sendiri melalui fitur keranjang dan checkout. Makanan yang telah dipesan customer otomatis masuk ke database milik restoran sehingga mempermudah koki dalam menyiapkan menu makanan.



*Cara Menjalankan Aplikasi :*
1. Mengunduh file DataRestoran.sql pada master branch folder /src/db
2. Membuat database yang bernama DataRestoran pada postgreSQL, lalu mengimport file DataRestoran.sql pada database DataRestoran
3. Mengubah pengaturan server postgreSQL menjadi sebagai berikut:
         user="postgres",
         password="123",
         host="127.0.0.1",
         port=5432
4. Membuka folder src pada master branch lalu run program melalui file Main.py

*Modul terimpementasikan:*
1. Modul Menu (DisplayMenuUI)
2. Modul Produk (TambahProduk, MenuGUI1, MenuGUI2, MenuGUI3, MenuGUI4, MenuGUI5, MenuGUI6)
3. Modul Keranjang (DeleteMenu, DisplayKeranjangUI)
4. Modul Checkout (DisplayStrukGUI)

*Penanggungjawab Modul:*

Verawati Esteria S. Simatupang - 18220002
1. Tampilan Halaman Utama (Main)
2. Menghapus Daftar Menu di Keranjang pada database (DeleteMenu)
3. Menambah Produk (TambahProduk)

Agnes Tamara - 18220010
1. Tampilan Daftar Menu GUI (DisplayMenuUI)
2. Tampilan Halaman Setiap Produk (MenuGUI1, MenuGUI2, MenuGUI3, MenuGUI4, MenuGUI5, MenuGUI6)

Christopher Jie - 18220052
1. Membuat database datamenurestoran dan datapesanancustomer 
2. Tampilan Daftar Menu Restoran dari Database (DisplayMenuUI)
3. Tampilan Daftar Menu Restoran GUI (DisplayMenuUI)
4. Fitur tambah/kurang barang(DisplayHalamanProduk)
5. Fitur total dan subtotal (Checkout)

Salimatussholati Az Zahra - 18220054
1. Fitur Pencarian Menu (DisplayMenuUI)

Michel Vito Adinugroho - 18220066
1. Tampilan Daftar Menu GUI (DisplayMenuUI)
2. Tampilan CheckOut GUI (DisplayStrukGUI)

Muhammad Rayfasa Candra - 18220076
1. Tampilan Keranjang (DisplayKeranjangUI)


*Daftar Tabel Basisdata :*

Tabel datamenurestoran(id_barang, nama_barang, deskripsi_barang, harga_barang)

Tabel datapesanancustomer(id_barang(foreign key), jumlah_barang, nama_barang, total_harga)
