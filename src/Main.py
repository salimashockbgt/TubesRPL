import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        
        root.geometry("1280x832")
        root.title("HALAMAN UTAMA")
        root.configure(bg = "#FFFFFF")


        canvas = Canvas(
            root,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            373.0,
            118.0,
            anchor="nw",
            text="Selamat Datang di MyFood",
            fill="#000000",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        canvas.create_text(
            603.0,
            179.0,
            anchor="nw",
            text="MyFood",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=522.0,
            y=302.0,
            width=238.60464477539062,
            height=53.02325439453125
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=522.0,
            y=389.4883728027344,
            width=238.60464477539062,
            height=53.02325439453125
        )
        root.resizable(False, False)
        root.mainloop()

if __name__ == "__main__":
    app = Main()
    Main.mainloop()
