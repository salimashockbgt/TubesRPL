from tkinter import *
import tkinter as tk

class TambahKurang(tk.Tk):
    #constructor
    def __init__(roo):
        super().__init__()
        def tambahkurang():
            root = Tk()
            root.title("MyFood")
            root.minsize(width=2000, height=2000)
            root.configure(bg="white")

            # def button_clicked():
            #     paketAyam_total = int(paketAyam_tambahKurang.get()) * 99999.99
            #     total_harga = paketAyam_total
            #     tagihan = Label()

            # product image
            # paketAyam = PhotoImage(file="images\halamanproduk.jpg")
            # paketAyam_image = Label(image=paketAyam, borderwidth=0)
            # paketAyam_image.place(x=50, y=130) # letaknya masih asal

            paketAyam_name = Label(text="Paket Ayam Meriah Komplit\n", font=("Arial", 12, "bold"), bg="white")
            paketAyam_name.place(x=600, y=470) # letaknya masih asal

            paketAyam_details = Label(text="Nasi + Ayam Goreng Paha/Dada + Tahu + Tempe\n", font=("Arial", 10, "normal"), bg="white")
            paketAyam_details.place(x=600, y=495) # letaknya masih asal

            paketAyam_details2 = Label(text="+ Sambal Bawang + Lalap\n", font=("Arial", 10, "normal"), bg="white")
            paketAyam_details2.place(x=600, y=515) # letaknya masih asal

            paketAyam_harga = Label(text="Rp99.999,99\n", font=("Arial", 10, "bold"), bg="white")
            paketAyam_harga.place(x=600, y=540) # letaknya masih asal

            paketAyam_jumlah = Label(text="Jumlah\n", font=("Arial", 10, "bold"), bg="white")
            paketAyam_jumlah.place(x=770, y=570) # letaknya masih asal

            paketAyam_tambahKurang = Spinbox(from_=0, to=10, width=5)
            paketAyam_tambahKurang.place(x=775, y=595)

            # tambahkan ke pesanan
            # pesan = Button(text="Tambahkan ke Pesanan", command=button_clicked)
            # pesan.place(x=210, y=560)

            root.mainloop()
        tambahkurang()