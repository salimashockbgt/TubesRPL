import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
<<<<<<< HEAD
import DisplayHalamanProduk.tambahKurang as produk
=======
import DisplayHalamanProduk.DisplayHalamanProdukGUI as produk
>>>>>>> a8ccf3e0e43b657029c632419c578429153c1ba6

class DisplayMenuGUI(tk.Tk):
    #constructor
    def __init__(roo):
        super().__init__()
        
        def displayMenu():
            #framing
            roo.geometry("2000x2000")
            roo.title("DAFTAR MENU")
            frame = Canvas(roo, height=100, width=100) 
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.5)

            #label judul
            Tops = Frame(roo,bg="white",width = 1600,height=50,relief=SUNKEN)
            Tops.pack(side=TOP)
            judul = Label(Tops, text="DAFTAR MENU ", font=("Times", 20, "bold"))
            judul.grid(row=0, column=0)

            #tombol back
            back=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Back", bg="Blue", command = lambda: roo.destroy())
            back.grid(row=4, column=0)

            #tombol halaman produk
            back=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Produk", bg="Blue", command = produk.TambahKurang)
            back.grid(row=3, column=0)

            # tombol halaman produk
            tombolProduk=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="details", bg="Blue", command = produk.DisplayHalamanProdukGUI)
            tombolProduk.grid(row=3, column=1)

            #program
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
            conn = getMenu()
            cursor = conn.cursor()
            query = 'SELECT * FROM datamenurestoran;'
            cursor.execute(query)
            def table(listbox):  #membuat tabel
                for i in range(0,total_rows):
                    for j in range(total_columns):
                        e =Label(listbox, width=50, fg='#3d8f17', #lebar isi tabel
                                font=('Times', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                        e.grid(row=i+1, column=j)
            rows = cursor.fetchall()
            total_rows = len(rows)
            total_columns = len(rows[0])

            listbox = Listbox(roo, width=10, height=5)  #kotak batasan GUI
            listbox["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times', size=20)
            listbox["font"] = ft
            listbox["fg"] = "#000"
            listbox["justify"] = "left"
            listbox.place(x=85, y=90, width=1420, height=140) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Nama Menu', 'Deskripsi Menu', 'Harga'] #judul data
            for k in range(4):
                e =Label(listbox, width=50, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel
            roo.mainloop()
        displayMenu() #test