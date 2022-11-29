import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.font as tkFont
import DisplayHalamanProduk.Menu1GUI as menu1
import DisplayHalamanProduk.Menu2GUI as menu2
import DisplayHalamanProduk.Menu3GUI as menu3
import DisplayHalamanProduk.Menu4GUI as menu4
import DisplayHalamanProduk.Menu5GUI as menu5
import DisplayHalamanProduk.Menu6GUI as menu6
import DisplayKeranjang.DisplayKeranjangUI as keranjang
import psycopg2

class DisplayMenuUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenuUI():
            roo.geometry("1280x832")
            roo.title("Menu")
            roo.configure(bg = "#FFFFFF")

            canvas = Canvas(
                roo,
                bg = "#FFFFFF",
                height = 832,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            canvas.create_text(
                200.0,
                119.0,
                anchor="nw",
                text="Daftar Menu",
                fill="#000000",
                font=("OpenSansRoman Bold", 40 * -1)
            )
            
            button_10 = Button(
                roo,
                text='1',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu1.Menu1GUI,
                relief="flat"
            )
            button_10.place(
                x=126.0,
                y=322.0,
                width=55.0,
                height=18.0
            )

            button_11 = Button(
                roo,
                text='3',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu3.Menu3GUI,
                relief="flat"
            )
            button_11.place(
                x=126.0,
                y=364.0,
                width=55.0,
                height=18.0
            )
   
            button_12 = Button(
                roo,
                text='4',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu4.Menu4GUI,
                relief="flat"
            )
            button_12.place(
                x=126.0,
                y=385.0,
                width=55.0,
                height=18.0
            )

            button_13 = Button(
                roo,
                text='5',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu5.Menu5GUI,
                relief="flat"
            )
            button_13.place(
                x=126.0,
                y=406.0,
                width=55.0,
                height=18.0
            )
            
            button_14 = Button(
                roo,
                text='2',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu2.Menu2GUI,
                relief="flat"
            )
            button_14.place(
                x=126.0,
                y=343.0,
                width=55.0,
                height=18.0
            )

           
            button_15 = Button(
                roo,
                text='6',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=menu6.Menu6GUI,
                relief="flat"
            )
            button_15.place(
                x=126.0,
                y=427.0,
                width=55.0,
                height=18.0
            )

            #back button
            button_17 = Button(
                roo,
                text='Back',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=lambda: roo.destroy(),
                relief="flat"
            )
            button_17.place(
                relx=0.42,
                rely=0.75,
                width=78.0,
                height=53.02325439453125
            )
            #  button keranjang
            buttonkeranjang = Button(
                roo, text="Lihat\nKeranjang", 
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=keranjang.DisplayKeranjangUI,
                relief="flat"
            )
            buttonkeranjang.place(
                relx=0.49,
                rely=0.75,
                width=78.0,
                height=53.02325439453125)
            
            #Update the listbox
            def update(data):
                my_list.delete(0, END)

                for item in data:
                    my_list.insert(END, item)
            #Update entry box with listbox clicked
            def fillout(event):
                my_entry.delete(0,END)
                #add clicked list item to entry box
                my_entry.insert(0, my_list.get(ACTIVE))
            #Create function to check entry vs listboc
            def check(event):
            # Grab what was typed
                typed = my_entry.get()
                if typed == '':
                    data = menu
                else:
                    data = []
                for item in menu:
                    if str(typed.lower()) in str(item.lower()):
                        data.append(item)
                #update our listbox with selected items
                update(data)
            def selectmenu():
                if (str(my_entry.get()) == "Nasi Goreng Ayam"):
                    menu1.Menu1GUI()
                elif (str(my_entry.get()) ==  "Nasi Timbel"):
                    menu2.Menu2GUI()
                elif (str(my_entry.get()) == "Nasi Uduk"):
                    menu3.Menu3GUI()
                elif (str(my_entry.get()) == "Teh Panas"):
                    menu4.Menu4GUI()
                elif (str(my_entry.get()) == "Es Teh"):
                    menu5.Menu5GUI()
                elif (str(my_entry.get()) == "Es Teh Manis/Teh manis"):
                    menu6.Menu6GUI()
    
            my_entry=Entry(roo, font=("Helvetica", 20))
            my_entry.pack()
            my_list = Listbox(roo, width=50)
            my_list.pack(pady=40)
            #tombolcari1=Button(canvas, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Cari", bg="Orange", command = selectmenu)
            #  button keranjang
            tombolcari = Button(
                roo, 
                text="Cari", 
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command= selectmenu,
                relief="flat"
            )
            tombolcari.place(
                relx=0.63,
                rely=0.006,
                width=78.0,
                height=30)
            
            #tombolcari.grid(row=1, column=0)
            #tombolcari.pack(padx=900, pady=70)

            # Create a list of menu
            menu = ["Nasi Goreng Ayam", "Nasi Timbel", "Nasi Uduk", "Teh Panas", "Es Teh", "Es Teh Manis/Teh manis"]
            update(menu)

            #Create a binding on the listbox onclick
            my_list.bind("<<ListboxSelect>>", fillout)

            #Create a binding on the entry box
            my_entry.bind("<KeyRelease>", check)
            
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
            query = 'SELECT id_barang, nama_barang, harga_barang FROM datamenurestoran;'
            cursor.execute(query)
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
            listbox.place(x=200, y=305, width=540, height=135) #batas buat kotak yang diisi tabel disesuaikan
            header=['ID', 'Nama Menu', 'Harga'] #judul data
            for k in range(3):
                e =Label(listbox, width=25, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove") #lebar judul tabel
                e.grid(row=0, column=k)
            table(listbox) #ubah data jadi tabel
            
            roo.resizable(False, False)
            roo.mainloop()
        displayMenuUI()
