import tkinter as tk
from tkinter import *
import DisplayMenu.DisplayMenuGUI as display
import DisplayKeranjang.DisplayKeranjangGUI as keranjang

#halaman utama
class Main(tk.Tk):
    #constructor
    def __init__(root):
        super().__init__()

        #framing
        root.geometry("2000x2000")
        root.title("HALAMAN UTAMA")

        frame = Canvas(root, height=100, width=100)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

        logo = Label(Tops, text= "MYFOOD", font=("Times", 10, "bold"))
        judul = Label(Tops, text="SELAMAT DATANG DI MYFOOD!!! ", font=("Times", 20, "bold"), fg = "#489012")
        gap = Label (frame, text=" ")

        #tombol bisa ditambah buat requirement baru
        daftarmenu=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Lihat Menu", bg="Blue", command = display.DisplayMenuGUI)
        daftarkeranjang=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Lihat Keranjang", bg="Blue", command = keranjang.DisplayKeranjangGUI)
        exit=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Exit", bg="Blue", command = lambda: root.quit())

        #jangan lupa digrid setelah tambah label/button
        judul.grid(row=0,column=0)
        logo.grid(row=1,column=0)
        gap.grid(row=1,column=0)
        daftarmenu.grid(row=2, column=0)
        daftarkeranjang.grid(row=3, column=0)
        exit.grid(row=7, column=0)

        root.mainloop()

#test
if __name__ == "__main__":
    app = Main()
    Main.mainloop()