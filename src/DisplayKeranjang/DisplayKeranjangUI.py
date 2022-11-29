import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as Menu
import CheckOut.DisplayStrukGUI as checkout
import DisplayKeranjang.DeleteMenu as deleteMenu
from tkinter import messagebox

class DisplayKeranjangUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayKeranjang():
            roo.geometry("1280x832")
            roo.title("Keranjang")

            frame = Canvas(roo, height=100, width=100) 
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.5)
            Tops = Frame(roo,bg="white",width = 1600,height=50,relief=SUNKEN)
            Tops.pack(side=TOP)

            # Judul halaman
            judul = Label(Tops, text="Keranjang", font=("Times", 20, "bold"))
            judul.grid(row=0, column=0)

            # program
            def getKeranjang():
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

            conn = getKeranjang()
            cursor = conn.cursor()
            query = 'SELECT * FROM datapesanancustomer;'
            cursor.execute(query)
            
            # Buat Tabel
            def table(listbox):  #membuat tabel
                for i in range(0,total_rows):
                    for j in range(total_columns):
                        e =Label(listbox, width=25, fg='#3d8f17', #lebar isi tabel
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
            listbox.place(x=300, y=122, width=710, height=135) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Jumlah', 'Nama Menu', 'Harga'] #judul data
            for k in range(4):
                e =Label(listbox, width=25, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel

            # Button
            hapusMenu = Button(roo, text = "Hapus Menu", bg= '#FBB43C',command=deleteMenu.DeleteMenu) # command : HapusMenu()
            hapusMenu.place(x=600, y=600)

            BackToMenu = Button(roo, text = "Kembali ke Menu", bg= '#FBB43C',command=Menu.DisplayMenuUI) # command : BackToMenu()
            BackToMenu.place(x = 360, y = 600)

            CheckOut = Button(roo, text = "Checkout", bg= '#FBB43C', command= checkout.DisplayStrukGUI) # command : CheckOut()
            CheckOut.place(x=850, y=600)
            
            def AddNotes():
                messagebox.showinfo('notes',"Notes has been sent to chef")

            my_entry=Entry(roo, font=("Helvetica", 20))
            my_entry.pack()
            tombolcari=Button(roo, padx=9,pady=9,bd=4, font=('Times', 16,'bold'), text="Notes", bg="Orange", command = AddNotes)
            tombolcari.place(x=800, y=20)

            roo.resizable(False, False)
            roo.mainloop()
        displayKeranjang()
