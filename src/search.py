from tkinter import *
root = Tk()
root.title('Menu MYFOOD')

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



my_label = Label(root, text="Start Typing...", font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)
my_entry=Entry(root, font=("Helvetica", 20))
my_entry.pack()
my_list = Listbox(root, width=50)
my_list.pack(pady=40)


# Create a list of menu
menu = ["Ayam Geprek", "Nasi Kebuli", "Mi Goreng", "Nasi Goreng", "Bebek Goreng"]
update(menu)

#Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

#Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()