import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DisplayMenuGUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayMenu():
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
                513.0,
                119.0,
                anchor="nw",
                text="Daftar Menu",
                fill="#000000",
                font=("OpenSansRoman Bold", 40 * -1)
            )

            button_image_10 = PhotoImage(
                file=relative_to_assets("button_10.png"))
            button_10 = Button(
                image=button_image_10,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_10 clicked"),
                relief="flat"
            )
            button_10.place(
                x=126.0,
                y=322.0,
                width=55.0,
                height=18.0
            )

            button_image_11 = PhotoImage(
                file=relative_to_assets("button_11.png"))
            button_11 = Button(
                image=button_image_11,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_11 clicked"),
                relief="flat"
            )
            button_11.place(
                x=126.0,
                y=364.0,
                width=55.0,
                height=18.0
            )

            button_image_12 = PhotoImage(
                file=relative_to_assets("button_12.png"))
            button_12 = Button(
                image=button_image_12,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_12 clicked"),
                relief="flat"
            )
            button_12.place(
                x=126.0,
                y=385.0,
                width=55.0,
                height=18.0
            )

            button_image_13 = PhotoImage(
                file=relative_to_assets("button_13.png"))
            button_13 = Button(
                image=button_image_13,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_13 clicked"),
                relief="flat"
            )
            button_13.place(
                x=126.0,
                y=406.0,
                width=55.0,
                height=18.0
            )

            button_image_14 = PhotoImage(
                file=relative_to_assets("button_14.png"))
            button_14 = Button(
                image=button_image_14,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_14 clicked"),
                relief="flat"
            )
            button_14.place(
                x=126.0,
                y=343.0,
                width=55.0,
                height=18.0
            )

            button_image_15 = PhotoImage(
                file=relative_to_assets("button_15.png"))
            button_15 = Button(
                image=button_image_15,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_15 clicked"),
                relief="flat"
            )
            button_15.place(
                x=126.0,
                y=427.0,
                width=55.0,
                height=18.0
            )

            button_image_16 = PhotoImage(
                file=relative_to_assets("button_16.png"))
            button_16 = Button(
                image=button_image_16,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_16 clicked"),
                relief="flat"
            )
            button_16.place(
                x=840.0,
                y=189.0,
                width=78.0,
                height=53.02325439453125
            )

            button_image_17 = PhotoImage(
                file=relative_to_assets("button_17.png"))
            button_17 = Button(
                image=button_image_17,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_17 clicked"),
                relief="flat"
            )
            button_17.place(
                x=601.0,
                y=621.0,
                width=78.0,
                height=53.02325439453125
            )

            entry_image_2 = PhotoImage(
                file=relative_to_assets("entry_2.png"))
            entry_bg_2 = canvas.create_image(
                640.0,
                215.51162719726562,
                image=entry_image_2
            )
            entry_2 = Entry(
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0
            )
            entry_2.place(
                x=457.0,
                y=189.0,
                width=366.0,
                height=51.02325439453125
            )
            roo.resizable(False, False)
            roo.mainloop()
        displayMenu()