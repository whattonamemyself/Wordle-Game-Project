import tkinter as tk
from tkinter import *
class Screen:   
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width = 1000, height = 600, bg = "black")
        self.canvas.pack()
        heading = Label(self.window, text = "Wordle", font = ("DIN Condensed", 35, "bold"), fg = "white", bg = "black")
        heading.place(x = 500, y = 30, anchor = CENTER)
        heading2 = Label(self.window, text = "+", font = ("Arial", 35), fg = "white", bg = "black")
        heading2.place(x = 550, y = 30, anchor = CENTER)
        self.squares = []
        for x in range(365, 640, 55):
            square = []
            for y in range(115, 440, 55):
                square.append([x,y,x+50,y-50])
            self.squares.append(square)
        for i in self.squares:
            for j in i:
                self.canvas.create_rectangle(j[0], j[1], j[2], j[3], fill = "#141414", outline = "#3c3c3c")
        self.alphabet = []
        for x in range(322, 682, 36):
            self.alphabet.append([x,415,x+32,460])
        for x in range(340, 664, 36):
            self.alphabet.append([x,465,x+32,510])
        for x in range(376, 628, 36):
            self.alphabet.append([x,515,x+32,560])
        self.letters = "qwertyuiopasdfghjklzxcvbnm".upper()
        for i,v in enumerate(self.alphabet):
            self.canvas.create_rectangle(v[0], v[1], v[2], v[3], fill = "#848484")
            x = (v[0]+v[2])/2
            y = (v[1]+v[3])/2
            self.canvas.create_text((x, y), text = self.letters[i], font = ("DIN Condensed", 20, "bold"), 
                                    fill = "white")
        self.window.mainloop()
    def squareCorrect(self, guess, pos):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#548c4c")
        self.window.mainloop()
    def letterCorrect(self, pos):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#548c4c")
    def squareNotCorrect(self, guess, pos):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#3c3c3c")
        self.window.mainloop()
    def letterNotCorrect(self, pos):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#3c3c3c")
    def squareMisplaced(self, guess, pos):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#b49c3c")
        self.window.mainloop()   
    def letterMisplaced(self, pos):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#b49c3c")         
screen = Screen()

