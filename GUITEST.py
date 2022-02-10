import tkinter as tk
class Screen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("2000x1000")
        self.window.configure(background="black")
        self.heading = tk.Label(self.window, font = "Rubik", height = 2, 
                            width = 8, text = "Wordle+", bg = "black", fg = "white")
        self.heading.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
        self.heading.pack()
        self.window.mainloop()
screen = Screen()