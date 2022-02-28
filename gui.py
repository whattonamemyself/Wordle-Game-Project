import tkinter as tk
from tkinter import *
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from game import markGuess
from wordsearchgui import main

window = Tk()
canvas = Canvas(width = 1000, height = 600, bg = "black")
class Screen:   
    def __init__(self, canvas, window, isHard):
        self.hasWon = False
        self.isHard = isHard
        self.window = window
        self.canvas = canvas
        self.alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")
        self.possible_words = WordBank("words_alpha.txt")
        options = WordBank("common5letter.txt")
        self.word = options.getRandom()
        # self.word = "train"
        self.currDisplayOptions = False
        self.currSettingsOptions = False
        print(self.word)
        self.requirements = [[], [], [], [], []]
        self.correct = [0, 0, 0, 0, 0]
        self.somewhere = []
        self.guess = 1
        self.canvas.bind_all('<KeyPress>',self.keyPressed)
        self.canvas.bind_all("<BackSpace>",self.delete)
        self.canvas.bind_all("<Return>",self.enter)
        self.canvas.pack()
        heading = Label(self.window, text = "Wordle", font = ("DIN Condensed", 35, "bold"), fg = "white", bg = "black")
        heading.place(x = 500, y = 30, anchor = CENTER)
        heading2 = Label(self.window, text = "+", font = ("Arial", 35), fg = "white", bg = "black")
        heading2.place(x = 550, y = 30, anchor = CENTER)
        options = Button(self.window, text = "Options", font = ("DIN Condensed", 20, "bold"), fg = "#427031", highlightbackground = "black", command = self.optionsDisplay)
        options.place(x = 825, y = 30, anchor = CENTER)
        settings = Button(self.window, text = "Settings", font = ("DIN Condensed", 20, "bold"), fg = "#427031", highlightbackground = "black", command = self.settingsDisplay)
        settings.place(x = 175, y = 30, anchor = CENTER)
        self.squares = []
        for y in range(115, 440, 55):
            square = []
            for x in range(365, 640, 55):
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
        self.current = ""
        for i,v in enumerate(self.alphabet):
            self.canvas.create_rectangle(v[0], v[1], v[2], v[3], fill = "#848484")
            x = (v[0]+v[2])/2
            y = (v[1]+v[3])/2
            self.canvas.create_text((x, y), text = self.letters[i], font = ("DIN Condensed", 20, "bold"), 
                                    fill = "white")
        self.window.mainloop()
    def squareCorrect(self, guess, pos, char):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#548c4c")
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 30, "bold"), 
                                    fill = "white")
    def letterCorrect(self, pos, char):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#548c4c")
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 20, "bold"), 
                                    fill = "white")
    def squareNotCorrect(self, guess, pos, char):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#3c3c3c")
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 30, "bold"), 
                                    fill = "white")
    def letterNotCorrect(self, pos, char):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#3c3c3c")
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 20, "bold"), 
                                    fill = "white")
    def squareMisplaced(self, guess, pos, char):
        coords = self.squares[guess][pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#b49c3c")  
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 30, "bold"), 
                                    fill = "white")  
    def letterMisplaced(self, pos, char):
        coords = self.alphabet[pos]
        self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill = "#b49c3c")      
        x, y = (coords[0]+coords[2])/2, (coords[1]+coords[3])/2
        self.canvas.create_text((x, y), text = char, font = ("DIN Condensed", 20, "bold"), 
                                    fill = "white") 
    def displayCurrentWord(self):
        row = self.squares[self.guess-1]
        for i in range(5):
            box = row[i]
            self.canvas.create_rectangle(box[0], box[1], box[2], box[3], fill = "#141414", outline = "#3c3c3c") 
            if i < len(self.current)    :
                x = (box[0]+box[2])/2
                y = (box[1]+box[3])/2
                self.canvas.create_text((x, y), text = self.current[i].upper(), font = ("DIN Condensed", 30, "bold"), fill = "white")
    def displayFinalWord(self):
        modified = WordleWord(self.current)
        markGuess(self.word, modified, self.alpha)
        for i in range(5):
            if modified.isCorrect(i):
                self.correct[i] = modified.charAt(i)
                for j in self.alpha.getWord():
                    if j != modified.charAt(i):
                        self.requirements[i].append(j)
                self.squareCorrect(self.guess-1, i, self.current[i].upper())
                self.alpha.setCorrect(self.alpha.posOf(self.current[i]))
            elif modified.isMisplaced(i):
                self.requirements[i].append(modified.charAt(i))
                self.somewhere.append(modified.charAt(i))
                self.squareMisplaced(self.guess-1, i, self.current[i].upper())
                if not self.alpha.isCorrect(self.alpha.posOf(self.current[i])):
                    self.alpha.setMisplaced(self.alpha.posOf(self.current[i]))
            else:
                for j in range(5):
                    if modified.charAt(j) != self.correct[j]:
                        if modified.charAt(j) not in self.somewhere:
                            self.requirements[j].append(modified.charAt(i))
                self.squareNotCorrect(self.guess-1,i, self.current[i].upper())
                if not self.alpha.isCorrect(self.alpha.posOf(self.current[i])) and not self.alpha.isCorrect(self.alpha.posOf(self.current[i])):
                    self.alpha.setNotUsed(self.alpha.posOf(self.current[i]))
        correctCount = 0
        for i in range(len(self.alpha.word)):
            if self.alpha.isCorrect(i):
                correctCount += 1
                self.letterCorrect(self.letters.lower().find(self.alpha.charAt(i)), self.alpha.charAt(i).upper())
            elif self.alpha.isMisplaced(i):
                self.letterMisplaced(self.letters.lower().find(self.alpha.charAt(i)), self.alpha.charAt(i).upper())
            elif self.alpha.isNotUsed(i):
                self.letterNotCorrect(self.letters.lower().find(self.alpha.charAt(i)), self.alpha.charAt(i).upper())
        self.hasWon = correctCount == 5
    def keyPressed(self, event):
        valid = False
        if event.char in self.letters or event.char in self.letters.lower() and not self.hasWon:
            if len(self.current) < 5:
                self.current += event.char.lower()
                self.displayCurrentWord()
    def delete(self, event):
        if len(self.current) > 0:
            self.current = self.current[:-1]
            self.displayCurrentWord()
    def enter(self, event):
        valid = False
        if len(self.current) == 5:
            if self.possible_words.contains(self.current):
                valid = True
                if self.isHard:
                    sw = self.somewhere[::]
                    for i in range(len(self.current)):
                        if self.current[i] in self.requirements[i]:
                            valid = False
                        if self.current[i] in sw and self.current[i] not in self.requirements[i]:
                            valid = True
                            sw.remove(self.current[i])
                    if sw != []:
                        valid = False
        if valid:
            self.displayFinalWord()
            self.guess += 1
            self.current = ""
    def optionsDisplay(self):
        if not self.currDisplayOptions:
            self.buttons = []
            wordsearch = Button(self.window, text = "Word Search", font = ("DIN Condensed", 10, "bold"), highlightbackground = "black", fg = "#427031", bg = "black", command = self.displayWordSearch)
            wordsearch.place(x = 825, y = 60, anchor = CENTER)
            self.buttons.append(wordsearch)
            self.currDisplayOptions = True
        else:
            for i in self.buttons:
                i.destroy()
            self.currDisplayOptions = False
    def newGame(self, isHard):
        self.window.destroy()
        window = Tk()
        canvas = Canvas(width = 1000, height = 600, bg = "black")
        screen = Screen(canvas, window, isHard)
    def settingsDisplay(self):
        if not self.currSettingsOptions:
            self.set = []
            hardmode = Button(self.window, text = "Hard Mode", font = ("DIN Condensed", 10, "bold"), highlightbackground = "black", fg = "#427031", bg = "black", command = lambda: self.newGame(True))
            hardmode.place(x = 175, y = 60, anchor = CENTER)
            self.set.append(hardmode)
            self.currSettingsOptions = True
        else:
            for i in self.set:
                i.destroy()
            self.currSettingsOptions = False
    def displayWordSearch(self):
        self.window.destroy()
        main()
screen = Screen(canvas, window, False)