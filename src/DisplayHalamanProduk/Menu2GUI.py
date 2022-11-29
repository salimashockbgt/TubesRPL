import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as display
import DisplayKeranjang.DisplayKeranjangUI as keranjang
import DisplayHalamanProduk.TambahProduk as tambah
from tkinter import messagebox

class Menu2GUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenu2():
            roo.geometry("1280x832")
            roo.title("Menu2")
            
            menu_name = Label(roo, text="Nasi Timbel\n", font=("Arial", 12, "bold"))
            menu_name.place(x=360, y=150)

            menu_details = Label(roo, text="Nasi berbentuk kerucut dengan ayam goreng\n", font=("Arial", 10, "normal"))
            menu_details.place(x=360, y=180)

            menu_harga = Label(roo, text="Rp25.000\n", font=("Arial", 10, "bold"))
            menu_harga.place(x=360, y=205)

            menu_jumlah = Label(roo, text="Jumlah\n", font=("Arial", 10, "bold"))
            menu_jumlah.place(x=605, y=280)

            spbox = Spinbox(roo, from_=0, to=10, width=5)
            spbox.place(x=610, y=300)

            # button tambah pesanan
            buttonTambahPesanan = Button(roo, text="Tambahkan ke Pesanan",command=lambda : tambah.TambahProduk(2, spbox.get(), "Nasi Timbel", 25000.0), bg= '#FBB43C')
            buttonTambahPesanan.place(x = 560, y = 350)

            #  button balik ke menu
            buttonback = Button(roo, text="Kembali ke Menu", command=display.DisplayMenuUI, bg= '#FBB43C')
            buttonback.place(x = 360, y = 400)

            #  button balik ke keranjang
            buttonkeranjang = Button(roo, text="Lihat Keranjang", command=keranjang.DisplayKeranjangUI, bg= '#FBB43C')
            buttonkeranjang.place(x = 800, y = 400)

            # button hapus produk
            buttonhapus = Button(roo, text="Hapus Barang", command=lambda:Hapus(), bg= '#FBB43C')
            buttonhapus.place(x = 500, y = 400)

            # button ubah kuantitas
            buttonubah = Button(roo, text="Ubah Kuantitas", command=lambda:UbahKuantitas(spbox.get()), bg= '#FBB43C')
            buttonubah.place(x = 650, y =400)
            
            def getMenu():
                    try:
                        return psycopg2.connect(
                            database="DataRestoran",
                            user="postgres",
                            password="123",
                            host="127.0.0.1",
                            port=5432,
                        )
                    except:
                        return False
            def Hapus():
                conn = getMenu()
                cursor = conn.cursor()
                query = "DELETE FROM datapesanancustomer WHERE id_barang = '2' "
                cursor.execute(query)
                conn.commit()
                count = cursor.rowcount
                messagebox.showinfo(count,"The item has been deleted")

            def UbahKuantitas(jumlah_barang):
                conn = getMenu()
                cursor = conn.cursor()
                query = "UPDATE datapesanancustomer SET jumlah_barang=%s WHERE id_barang = '2' "
                cursor.execute(query,(jumlah_barang))
                conn.commit()
                count = cursor.rowcount
                messagebox.showinfo(count,"The quantity has been changed")              

            roo.resizable(False, False)
            roo.mainloop()
        displayMenu2()
