import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from math import *

class DisplayStrukGUI(tk.Tk):
    #constructor
    def __init__(roo):
        super().__init__()
        
        def displayStruk():
            #framing
            roo.geometry("2000x2000")
            roo.title("STRUK")
            frame = Canvas(roo, height=100, width=100) 
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.8)

            #label judul
            Tops = Frame(roo,bg="white",width = 1600,height=50,relief=SUNKEN)
            Tops.pack(side=TOP)
            judul = Label(Tops, text="Pesanan anda ", font=("Times", 20, "bold"))
            judul.grid(row=0, column=0)
            
            #label total harga pesanan
            texttotalharga = Label(roo, text="Total Harga Pesanan", font=("Times", 20, "bold"))
            texttotalharga.place(anchor='center', relx=0.5, rely=0.7)

            #label selamat menikmati
            textslm = Label(roo, text="Selamat Menikmati", font=("Times", 15, "bold"))
            textslm.place(anchor='center', relx=0.5, rely=0.85)
            
            #ambil data pesanan customer
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
            query = 'SELECT id_barang, jumlah_barang, nama_barang, harga_barang, (jumlah_barang*harga_barang) as total_harga FROM datapesanancustomer;'
            cursor.execute(query)
            
            #membuat tabel
            def table(listbox):  
                for i in range(0,total_rows):
                    for j in range(total_columns):
                        e =Label(listbox, width=30, fg='#3d8f17', #warna tulisan
                                font=('Times', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                        e.grid(row=i+1, column=j)
            rows = cursor.fetchall()
            total_rows = len(rows)
            total_columns = len(rows[0])

            listbox = Listbox(roo, width=5, height=5, fg='#ffffff', bg='#f0f0f0')  #kotak batasan GUI
            listbox["borderwidth"] = "0px"
            ft = tkFont.Font(family='Times', size=20)
            listbox["font"] = ft
            listbox["fg"] = "#e27013"
            listbox["justify"] = "left"
            listbox.place(x=100, y=75, width=1500, height=200) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Jumlah', 'Nama Makanan', 'Harga Satuan', 'Total Harga'] #judul data
            
            for k in range(5):
                e =Label(listbox, width=30, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel

            def Subtotal():
                query = "SELECT SUM(jumlah_barang*harga_barang) FROM datapesanancustomer"
                cursor.execute(query)
                conn.commit()
                result = cursor.fetchone()
                return result[0]

            #label harga sementara total harga pesanan
            biaya = Label(roo, text=str(Subtotal()),fg='#e27013', font=("Times", 20, "bold"))
            biaya.place(anchor='center', relx=0.5, rely=0.75)

            buttonback = Button(roo, text="Print Struk", command=lambda: roo.quit(), bg= '#FBB43C')
            buttonback.place(x=900,y=530)
            roo.mainloop()

        displayStruk() #test
