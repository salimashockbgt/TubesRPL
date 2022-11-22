import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
import DisplayHalamanProduk.tambahKurang as button

i=0

class DisplayHalamanProdukGUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayHalamanProduk():
            roo.geometry("2000x2000")
            roo.title("DAFTAR PRODUK")
            frame = Canvas(roo, height=100, width=100)
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.5)

            paketAyam_name = Label(roo, text="Nasi Goreng Ayam\n", font=("Arial", 12, "bold"))
            paketAyam_name.place(x=600, y=470) # letaknya masih asal

            paketAyam_details = Label(roo, text="Nasi goreng khas My Food dengan suwiran ayam\n", font=("Arial", 10, "normal"))
            paketAyam_details.place(x=600, y=495) # letaknya masih asal

            paketAyam_details2 = Label(roo, text="Rp25.000\n", font=("Arial", 10, "bold"))
            paketAyam_details2.place(x=600, y=515) # letaknya masih asal

            paketAyam_harga = Label(roo, text="\n", font=("Arial", 10, "normal"))
            paketAyam_harga.place(x=600, y=540) # letaknya masih asal

            paketAyam_jumlah = Label(roo, text="Jumlah\n", font=("Arial", 10, "bold"))
            paketAyam_jumlah.place(x=770, y=570) # letaknya masih asal

        def increment():
            global i
            i = i+1
            roo.label.config(text=i)
        
        def decrement():
            global i
            i = i-1
            roo.label.config(text=i)

        roo.buttonTambah = Button(roo, text="+", command=increment)
        roo.buttonTambah.pack()
        roo.buttonTambah.configure(bg="white")

        roo.buttonKurang = Button(roo, text="-", command=decrement)
        roo.buttonKurang.pack()
        roo.buttonKurang.configure(bg="white")

        roo.label = Label(roo, text= i, font=("Arial", 100))
        roo.label.pack()


        roo.mainloop()
        displayHalamanProduk() #test