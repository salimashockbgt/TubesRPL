from tkinter import *
import DisplayMenu.DisplayMenuGUI as display


#halaman utama
root = Tk()
root.geometry("2000x2000")


frame = Canvas(root, height=100, width=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

logo = Label(frame, text= "MYFOOD", font=("Times", 10, "bold"))
judul = Label(frame, text="SELAMAT DATANG DI MYFOOD!!! ", font=("Times", 20, "bold"))
gap = Label (frame, text=" ")
daftarmenu=Button(frame, padx=16,pady=16,bd=4, font=('Times', 16,'bold'), text="Lihat Menu", bg="Blue", command = display.displayMenu)

judul.grid(row=0,column=0)
gap.grid(row=1,column=0)
logo.grid(row=4,column=0)
daftarmenu.grid(row=2, column=0)

root.mainloop()
