import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DisplayMenu6GUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenu6():
            roo.geometry("1280x832")
            roo.title("Menu6")
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
                379.0,
                438.0,
                anchor="nw",
                text="Es Teh Manis/Teh Manis",
                fill="#000000",
                font=("OpenSansRoman Bold", 20 * -1)
            )

            canvas.create_text(
                604.0,
                563.0,
                anchor="nw",
                text="Jumlah",
                fill="#000000",
                font=("OpenSansRoman Bold", 20 * -1)
            )

            canvas.create_text(
                379.0,
                518.0,
                anchor="nw",
                text="Rp4.000,00",
                fill="#000000",
                font=("OpenSansRoman Bold", 20 * -1)
            )

            canvas.create_text(
                379.0,
                478.0,
                anchor="nw",
                text="Teh panas/es teh ditambah gula",
                fill="#000000",
                font=("OpenSansRoman Regular", 20 * -1)
            )

            entry_image_1 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
            entry_bg_1 = canvas.create_image(
                639.5,
                623.0,
                image=entry_image_1
            )
            entry_1 = Text(
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0
            )
            entry_1.place(
                x=590.0,
                y=603.0,
                width=99.0,
                height=38.0
            )

            button_image_5 = PhotoImage(
                file=relative_to_assets("button_5.png"))
            button_5 = Button(
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_5 clicked"),
                relief="flat"
            )
            button_5.place(
                x=689.0,
                y=603.0,
                width=69.0,
                height=40.0
            )

            button_image_6 = PhotoImage(
                file=relative_to_assets("button_6.png"))
            button_6 = Button(
                image=button_image_6,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_6 clicked"),
                relief="flat"
            )
            button_6.place(
                x=97.0,
                y=733.0,
                width=180.0,
                height=40.0
            )

            button_image_7 = PhotoImage(
                file=relative_to_assets("button_7.png"))
            button_7 = Button(
                image=button_image_7,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_7 clicked"),
                relief="flat"
            )
            button_7.place(
                x=521.0,
                y=603.0,
                width=69.0,
                height=40.0
            )

            button_image_8 = PhotoImage(
                file=relative_to_assets("button_8.png"))
            button_8 = Button(
                image=button_image_8,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_8 clicked"),
                relief="flat"
            )
            button_8.place(
                x=1029.0,
                y=733.0,
                width=180.0,
                height=40.0
            )

            button_image_9 = PhotoImage(
                file=relative_to_assets("button_9.png"))
            button_9 = Button(
                image=button_image_9,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_9 clicked"),
                relief="flat"
            )
            button_9.place(
                x=550.0,
                y=658.0,
                width=180.0,
                height=40.0
            )

            image_image_6 = PhotoImage(
                file=relative_to_assets("image_6.png"))
            image_6 = canvas.create_image(
                639.0,
                267.0,
                image=image_image_6
            )
            roo.resizable(False, False)
            roo.mainloop()
        displayMenu6()