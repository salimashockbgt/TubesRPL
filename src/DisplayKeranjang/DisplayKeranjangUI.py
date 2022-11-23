import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psycopg2
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import DisplayMenu.DisplayMenuUI as display
import CheckOut.DisplayStrukUI.py as struk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DisplayKeranjangGUI(tk.Tk):
    def __init__(roo):
        super().__init__()

        def displayKeranjang():
            roo.geometry("1280x832")
            roo.title("Keranjang")
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
                538.0,
                119.0,
                anchor="nw",
                text="Keranjang",
                fill="#000000",
                font=("OpenSansRoman Bold", 40 * -1)
            )
            
            button_3 = Button(
                roo,
                text='Kembali ke Menu',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=display.DisplayMenuUI,
                relief="flat"
            )
            button_3.place(
                x=97.0,
                y=733.0,
                width=180.0,
                height=40.0
            )
            
            button_4 = Button(
                roo,
                text='CheckOut',
                bg= '#FBB43C',
                borderwidth=0,
                highlightthickness=0,
                command=struk.DisplayStrukUI,
                relief="flat"
            )
            button_4.place(
                x=1029.0,
                y=733.0,
                width=180.0,
                height=40.0
            )
            roo.resizable(False, False)
            roo.mainloop()
        displayKeranjang()
