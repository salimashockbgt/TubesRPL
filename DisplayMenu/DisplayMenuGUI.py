from tkinter import *
import tkinter.font as tkFont
import psycopg2

def displayMenu():
    roo = Tk()
    roo.geometry("2000x2000")
    roo.title('Daftar Menu')
    conn = psycopg2.connect(database="DataRestoran",
                            user="postgres",
                            password="123",
                            host="127.0.0.1",
                            port=5432,)
    cursor = conn.cursor()
    query = 'SELECT * FROM datamenurestoran;'
    cursor.execute(query)
    
    def table(listbox):  #membuat tabel
        for i in range(0,total_rows):
            for j in range(total_columns):
                e =Label(listbox, width=50, fg='#3d8f17',
                          font=('Times', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                e.grid(row=i+1, column=j)
    rows = cursor.fetchall()
    total_rows = len(rows)
    total_columns = len(rows[0])

    listbox = Listbox(roo, width=10, height=5)  #kotak batasa GUI
    listbox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=20)
    listbox["font"] = ft
    listbox["fg"] = "#000"
    listbox["justify"] = "center"
    listbox.place(x=50, y=50, width=3000, height=300)
    header=['id', 'nama menu', 'deskripsi menu', 'harga'] #judul data
    for k in range(4):
        e =Label(listbox, width=50, fg='#e27013',font=('Times', 10, 'bold'), text=header[k], borderwidth=1, relief="groove")
        e.grid(row=0, column=k)
    table(listbox) #ubah data jadi tabel
    roo.mainloop()

