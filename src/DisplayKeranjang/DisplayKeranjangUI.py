import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuGUI as Menu
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
                        e =Label(listbox, width=50, fg='#3d8f17', #lebar isi tabel
                                font=('Times', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                        e.grid(row=i+1, column=j)
            rows = cursor.fetchall()
            total_rows = len(rows)
            total_columns = len(rows[0])

            listbox = Listbox(roo, width=10, height=5, bg='#f0f0f0')  #kotak batasan GUI
            listbox["borderwidth"] = "0px"
            ft = tkFont.Font(family='Times', size=20)
            listbox["font"] = ft
            listbox["fg"] = "#000"
            listbox["justify"] = "left"
            listbox.place(x=85, y=90, width=1420, height=140) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Jumlah', 'Nama Menu', 'Harga'] #judul data
            for k in range(4):
                e =Label(listbox, width=50, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel

            # Button
            #  Tambahin Command, Benerin Warna dan Ukuran
            tombolTambah = Button(roo, text = "+",fg ='white', bg ='blue') # command : TambahKuantitas()
            tombolTambah.place(x = 750, y = 600)

            tombolKurang = Button(roo, text = "-",fg ='white', bg ='blue') # command : KurangiKuantitas()
            tombolKurang.place(x = 775, y = 600)

            hapusMenu = Button(roo, text = "hapus menu",fg ='white', bg = 'blue') # command : HapusMenu()
            hapusMenu.place(x = 725, y = 620)

            BackToMenu = Button(roo, text = "kembali ke daftar menu",fg ='white', bg ='blue',command=Menu.DisplayMenuGUI) # command : BackToMenu()
            BackToMenu.place(x = 50, y = 675)

            CheckOut = Button(roo, text = "checkout",fg ='white', bg ='blue', command= checkout.DisplayStrukGUI) # command : CheckOut()
            CheckOut.place(x = 1400, y = 675)

            # roo.configure(bg = "#FFFFFF")


            # canvas = Canvas(
            #     roo,
            #     bg = "#FFFFFF",
            #     height = 832,
            #     width = 1280,
            #     bd = 0,
            #     highlightthickness = 0,
            #     relief = "ridge"
            # )

            # canvas.place(x = 0, y = 0)
            # canvas.create_text(
            #     538.0,
            #     119.0,
            #     anchor="nw",
            #     text="Keranjang",
            #     fill="#000000",
            #     font=("OpenSansRoman Bold", 40 * -1)
            # )

            # button_image_3 = PhotoImage(
            #     file=relative_to_assets("button_3.png"))
            # button_3 = Button(
            #     image=button_image_3,
            #     borderwidth=0,
            #     highlightthickness=0,
            #     command=lambda: print("button_3 clicked"),
            #     relief="flat"
            # )
            # button_3.place(
            #     x=97.0,
            #     y=733.0,
            #     width=180.0,
            #     height=40.0
            # )

            # button_image_4 = PhotoImage(
            #     file=relative_to_assets("button_4.png"))
            # button_4 = Button(
            #     image=button_image_4,
            #     borderwidth=0,
            #     highlightthickness=0,
            #     command=lambda: print("button_4 clicked"),
            #     relief="flat"
            # )
            # button_4.place(
            #     x=1029.0,
            #     y=733.0,
            #     width=180.0,
            #     height=40.0
            # )
            roo.mainloop()
        displayKeranjang()