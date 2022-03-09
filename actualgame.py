from wordbank import WordBank
from gui import Screen
from tkinter import *
from wordsearchgui import WSGUI
from wordsearch import WordSearch
from inputwrapper import InputWrapper
from settings import SettingsDisplay
from stats import StatsDisplayer
import button

all_words = WordBank("common5letter.txt")
displaySettings = None
statsDisplayer = None
screen = None
window = None
canvas = None
inputs = None
mode = 0

inGame = False

def gameOver(tries):
    global window
    if tries == -1:
        window.after(1000, gameover, 0, 0)
    else:
        window.after(1000, gameover, 1, tries)
def gameover(win, tries):
    global displaySettings 
    global statsDisplayer 
    global screen
    global inGame
    inGame = False
    statsDisplayer.updateStats(win, tries)
    statsDisplayer.open()

def stop():
    global displaySettings 
    global statsDisplayer 
    global screen
    screen.stop()

def start():
    global displaySettings 
    global statsDisplayer 
    global screen
    screen.start()

def newgame():
    global screen
    global canvas
    global mode
    global all_words
    global inputs
    global inGame
    if inGame:
        statsDisplayer.updateStats(0, 0)
    inGame = True
    if screen != None:
        screen.end()
        screen = None
    if mode == 0:
        word = all_words.getRandom()
        screen = Screen(canvas, window, gameOver, False, word, 6)
    else:
        ws = WordSearch(16,16)
        ws.genWordSearch()
        print(ws.getTarget())
        screen = WSGUI(ws, inputs, canvas, window, gameOver, False)
        screen.start()

def actualgame():
    global displaySettings 
    global statsDisplayer 
    global screen
    global window
    global canvas
    global inputs

    window = Tk()
    canvas = Canvas(window, width = 1000, height = 600, bg = "black")
    canvas.pack()
    inputs = InputWrapper(canvas)
    
    displaySettings = SettingsDisplay(canvas, window, inputs, screen)
    statsDisplayer = StatsDisplayer(canvas, window, inputs, start, stop, "uwu", 6)

    canvas.create_rectangle(0,0,50,50,outline = "", fill = "red")
    newGameButton = button.Button(inputs, window, newgame, 0, 0, 50, 50)
    newgame()
    window.mainloop()
actualgame()