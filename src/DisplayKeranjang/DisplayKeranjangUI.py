import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as Menu
import CheckOut.DisplayStrukGUI as checkout

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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

            

            # Atur Posisi, Grid, Scroll

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
            listbox.place(x=200, y=322, width=710, height=100) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Jumlah', 'Nama Menu', 'Harga'] #judul data
            for k in range(4):
                e =Label(listbox, width=25, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel

            # Button
            hapusMenu = Button(roo, text = "Hapus Menu", bg= '#FBB43C') # command : HapusMenu()
            hapusMenu.place(anchor='center', relx=0.5, rely=0.7)

            BackToMenu = Button(roo, text = "Kembali ke Menu", bg= '#FBB43C',command=Menu.DisplayMenuUI) # command : BackToMenu()
            BackToMenu.place(anchor='center', relx=0.45, rely=0.80)

            CheckOut = Button(roo, text = "Checkout", bg= '#FBB43C', command= checkout.DisplayStrukGUI) # command : CheckOut()
            CheckOut.place(anchor='center', relx=0.55, rely=0.80)
            
            roo.resizable(False, False)
            roo.mainloop()
        displayKeranjang()