from tkinter import *
import tkinter.font as tkFont
import psycopg2

def displayKeranjang():
    roo = Tk() # framing
    roo.geometry("2000x2000")
    roo.title("DAFTAR PESANAN")

    frame = Canvas(roo, height=100, width=100) 
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    Tops = Frame(roo,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    # Judul halaman
    judul = Label(Tops, text="Keranjang", font=("Times", 20, "bold"))
    judul.grid(row=0, column=0)

    # Menampilkan Pesanan Customer (Nama + Kuantitas)
        # ini masih agak bingung, ngambil dr array objeknya apa gmn dah


    # Button
    #  Tambahin Command, Benerin Warna dan Ukuran
    tombolTambah = Button(roo, text = "+",fg ='white', bg ='blue',padx = 5, pady=5) # command : TambahKuantitas()
    tombolTambah.pack() 

    tombolKurang = Button(roo, text = "-",fg ='white', bg ='blue',padx = 5, pady=5) # command : KurangiKuantitas()
    tombolKurang.pack()

    hapusMenu = Button(roo, text = "hapus menu",fg ='white', bg ='blue',padx = 15) # command : HapusMenu()
    hapusMenu.pack()

    BackToMenu = Button(roo, text = "kembali ke daftar menu",fg ='white', bg ='blue') # command : BackToMenu()
    BackToMenu.pack()

    CheckOut = Button(roo, text = "checkout",fg ='white', bg ='blue') # command : CheckOut()
    CheckOut.pack()

    # Atur Posisi, Grid, Scroll




    roo.mainloop()

displayKeranjang()