import tkinter as tk
from tkinter import *
class Screen:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width = 2000, height = 1000)
        self.canvas.pack()
        self.heading = Label(self.window, text = "Wordle +", font = "Rubik 40 bold", fg = "white")
        self.heading.place(x = 960, y = 30, anchor = CENTER)
        self.squares = []
        for x in range(770, 1170, 80):
            square = []
            for y in range(175, 605, 80):
                square.append([x,y,x+70,y-70])
            self.squares.append(square)
        for i in self.squares:
            for j in i:
                self.canvas.create_rectangle(j[0], j[1], j[2], j[3])
        self.window.mainloop()
screen = Screen()

