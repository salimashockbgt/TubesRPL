import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as display
import DisplayKeranjang.DisplayKeranjangUI as keranjang

from DisplayHalamanProduk.TambahProduk import TambahProduk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Menu1GUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenu1():
            roo.geometry("1280x832")
            roo.title("Menu1")

            paketAyam_name = Label(roo, text="Nasi Goreng Ayam\n", font=("Arial", 12, "bold"))
            paketAyam_name.place(x=600, y=470) # letaknya masih asal

            paketAyam_details = Label(roo, text="Nasi goreng khas My Food dengan suwiran ayam\n", font=("Arial", 10, "normal"))
            paketAyam_details.place(x=600, y=495) # letaknya masih asal

            paketAyam_details2 = Label(roo, text="Rp25.000\n", font=("Arial", 10, "bold"))
            paketAyam_details2.place(x=600, y=515) # letaknya masih asal

            paketAyam_harga = Label(roo, text="\n", font=("Arial", 10, "normal"))
            paketAyam_harga.place(x=600, y=540) # letaknya masih asal

            paketAyam_jumlah = Label(roo, text="Jumlah\n", font=("Arial", 10, "bold"))
            paketAyam_jumlah.pack()
            paketAyam_jumlah.place(x=770, y=570) # letaknya masih asal
            # L1 = Label(roo, text="User Name")
            # L1.pack( side = LEFT)
            # E1 = Entry(roo, bd =5)
            # E1.pack(side = RIGHT)

            # jumlah=IntVar()
            # entri = Entry(roo,textvariable=jumlah, width=10)
            # entri.pack()
            # entri.place(x=775, y=595)

            # var=IntVar()
            # #spinbox
            # def spbox():
            #     print()
            # menu1box = Spinbox(roo, from_=0, to=10, width=5, command= print(menu1box.get()))
            # menu1box.place(x=775, y=595)

            current_value = tk.StringVar(value=0)
            spbox = Spinbox(roo, from_=0, to=10, width=5, textvariable=current_value, wrap=True)
            spbox.pack()
            spbox.place(x=775, y=595)
        
            addtocart = TambahProduk(1, current_value.get(), "Nasi Goreng Ayam", 25000.0)
            # button tambah pesanan
            buttonTambahPesanan = Button(roo, text="Tambahkan ke Pesanan",command=addtocart, bg= '#FBB43C')
            buttonTambahPesanan.pack()
            buttonTambahPesanan.place(anchor='center', relx=0.5, rely=0.75)

            #  button balik ke menu
            buttonback = Button(roo, text="Kembali ke Menu", command=display.DisplayMenuUI, bg= '#FBB43C')
            buttonback.pack()
            buttonback.place(anchor='center', relx=0.45, rely=0.85)

            #  button balik ke keranjang
            buttonkeranjang = Button(roo, text="Lihat Keranjang", command=keranjang.DisplayKeranjangUI, bg= '#FBB43C')
            buttonkeranjang.pack()
            buttonkeranjang.place(anchor='center', relx=0.55, rely=0.85)

            roo.resizable(False, False)
            roo.mainloop()
        displayMenu1()
        
