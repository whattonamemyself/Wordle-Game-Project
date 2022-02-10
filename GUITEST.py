import tkinter as tk
class Screen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("2000x1000")
        self.window.configure(background="#2c373d")
        self.tab = tk.Label(self.window, font = "Rubik", height = 1, 
                            width = 250, text = "Wordle+", bg  = "#445464", 
                            fg = "white")
        self.tab.pack()
        self.window.mainloop()
screen = Screen()