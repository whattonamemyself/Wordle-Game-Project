import tkinter as tk
class Screen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("2000x1000")
        self.window.configure(background="white")
        self.heading = tk.Label(font = "Rubik")
        self.window.mainloop()
screen = Screen()