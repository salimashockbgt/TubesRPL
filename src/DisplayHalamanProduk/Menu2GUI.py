import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as display
import DisplayKeranjang.DisplayKeranjangUI as keranjang
import DisplayHalamanProduk.TambahProduk as tambah

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Menu2GUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenu2():
            roo.geometry("1280x832")
            roo.title("Menu2")
            
            paketAyam_name = Label(roo, text="Nasi Timbel\n", font=("Arial", 12, "bold"))
            paketAyam_name.place(x=600, y=470) # letaknya masih asal

            paketAyam_details = Label(roo, text="Nasi berbentuk kerucut dengan ayam goreng\n", font=("Arial", 10, "normal"))
            paketAyam_details.place(x=600, y=495) # letaknya masih asal

            paketAyam_details2 = Label(roo, text="Rp25.000\n", font=("Arial", 10, "bold"))
            paketAyam_details2.place(x=600, y=515) # letaknya masih asal

            paketAyam_harga = Label(roo, text="\n", font=("Arial", 10, "normal"))
            paketAyam_harga.place(x=600, y=540) # letaknya masih asal

            paketAyam_jumlah = Label(roo, text="Jumlah\n", font=("Arial", 10, "bold"))
            paketAyam_jumlah.place(x=770, y=570)

            spbox = Spinbox(roo, from_=0, to=10, width=5)
            spbox.place(x=775, y=595)

        
            # button tambah pesanan
            buttonTambahPesanan = Button(roo, text="Tambahkan ke Pesanan",command=lambda jumlah_barang=spbox.get() : tambah.TambahProduk(2, jumlah_barang, "Nasi Timbel", 25000.0), bg= '#FBB43C')
            buttonTambahPesanan.pack()
            buttonTambahPesanan.place(anchor='center', relx=0.5, rely=0.75)

            #  button balik ke menu
            buttonback = Button(roo, text="Kembali ke Menu", command=display.DisplayMenuUI, bg= '#FBB43C')
            buttonback.pack()
            buttonback.place(anchor='center', relx=0.45, rely=0.80)

            #  button balik ke keranjang
            buttonkeranjang = Button(roo, text="Lihat Keranjang", command=keranjang.DisplayKeranjangUI, bg= '#FBB43C')
            buttonkeranjang.pack()
            buttonkeranjang.place(anchor='center', relx=0.55, rely=0.80)

            roo.resizable(False, False)
            roo.mainloop()
        displayMenu2()