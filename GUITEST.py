import tkinter as tk
class Screen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("2000x1000")
        self.window.configure(background="white")
        self.tab = tk.Label(self.window, font = "Rubik", height = 2, 
                            width = 3, text = "Wordle+", fg = "black")
        self.tab.pack()
        self.window.mainloop()
screen = Screen()