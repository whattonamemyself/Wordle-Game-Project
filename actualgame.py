from wordbank import WordBank
from gui import Screen
from tkinter import *
from wordsearchgui import WSGUI
from wordsearch import WordSearch
from inputwrapper import InputWrapper
from settings import SettingsDisplay
from stats import StatsDisplayer

all_words = WordBank("common5letter.txt")
displaySettings = None
statsDisplayer = None
screen = None
window = None
canvas = None
inputs = None
mode = 0

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
    statsDisplayer.updateStats(win, tries)
    #newgame()
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

    newgame()
    window.mainloop()
actualgame()