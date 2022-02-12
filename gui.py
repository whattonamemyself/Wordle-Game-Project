import tkinter as tk
from tkinter import *
class Screen:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width = 1000, height = 600, bg = "black")
        self.canvas.pack()
        self.heading = Label(self.window, text = "WORDLE +", font = "Rubik 40 bold", fg = "white", bg = "black")
        self.heading.place(x = 500, y = 30, anchor = CENTER)
        self.squares = []
        for x in range(380, 630, 50):
            square = []
            for y in range(115, 415, 50):
                square.append([x,y,x+40,y-40])
            self.squares.append(square)
        for i in self.squares:
            for j in i:
                self.canvas.create_rectangle(j[0], j[1], j[2], j[3], outline = "white")
        test = Button(self.window, text = "PRESS ME", fg = "white", bg = "black", command = self.window.quit)
        test.pack()
        self.window.mainloop()
    def squareCorrect(self, guess, pos):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "green", outline = "white")
        self.window.mainloop()
screen = Screen()

screen.squareCorrect(3, 2)

