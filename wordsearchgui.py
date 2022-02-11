import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper

class WSGUI():
    def __init__(ws):
        self.wordsearch = ws

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    uwu = "uwu"
    print("HII")
    window.mainloop()
if __name__ == "__main__":
    main()
