import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2

class DisplayHalamanProdukGUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayHalamanProduk():
            roo.geometry("2000x2000")
            
            frame = Canvas(roo, height=100, width=100)
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.5)

            paketAyam_name = Label(roo, text="Paket Ayam Meriah Komplit\n", font=("Arial", 12, "bold"))
            paketAyam_name.place(x=600, y=470) # letaknya masih asal

            paketAyam_details = Label(roo, text="Nasi + Ayam Goreng Paha/Dada + Tahu + Tempe\n", font=("Arial", 10, "normal"))
            paketAyam_details.place(x=600, y=495) # letaknya masih asal

            paketAyam_details2 = Label(roo, text="+ Sambal Bawang + Lalap\n", font=("Arial", 10, "normal"))
            paketAyam_details2.place(x=600, y=515) # letaknya masih asal

            paketAyam_harga = Label(roo, text="Rp99.999,99\n", font=("Arial", 10, "bold"))
            paketAyam_harga.place(x=600, y=540) # letaknya masih asal

            paketAyam_jumlah = Label(roo, text="Jumlah\n", font=("Arial", 10, "bold"))
            paketAyam_jumlah.place(x=770, y=570) # letaknya masih asal

            # paketAyam_tambahKurang = Spinbox(from_=0, to=10, width=5)
            # paketAyam_tambahKurang.place(x=775, y=595)

            def getHalamanProduk():
                try:
                    return psycopg2.connect(
                        database="DataRestoran",
                        user="postgres",
                        password="Kimjongin140194",
                        host="127.0.0.1",
                        port=5432,
                    )
                except:
                    return False
            
            conn = getHalamanProduk()
            cursor = conn.cursor()
            query = 'SELECT * FROM datapesanancustomer;'
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
        displayHalamanProduk() #test