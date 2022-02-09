import tkinter as tk
class Screen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("2000x1000")
        self.tab = tk.Button(self.window, height = 1, width = 250, 
                             text = "Wordle+", bg  = "green", font = "SF", 
                             command = self.hello)
        self.tab.pack()
        self.window.mainloop()
    def hello(self):
        print("hello")
screen = Screen()