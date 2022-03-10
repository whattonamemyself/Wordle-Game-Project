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
pause = False
mode = 0

inGame = False

"""
gameOver
Input: int
tries = number of tries, -1 if lose
"""
def gameOver(tries):
    global window
    if tries == -1:
        window.after(1000, gameover, 0, 0)
    else:
        window.after(1000, gameover, 1, tries)

#helper function, dont call
def gameover(win, tries):
    global displaySettings 
    global statsDisplayer 
    global screen
    global inGame
    inGame = False
    statsDisplayer.updateStats(win, tries)
    statsDisplayer.open()

# stops the current running game
def stop():
    global displaySettings 
    global statsDisplayer 
    global screen
    global pause
    pause = True
    screen.stop()
    statsDisplayer.stop()
    displaySettings.stop()

#starts the current running game
def start():
    global displaySettings 
    global statsDisplayer 
    global screen
    global pause
    pause = False
    screen.start()
    statsDisplayer.start()
    displaySettings.start()

#creates a new game
def newgame():
    if pause:
        return
    global screen
    global canvas
    global mode
    global all_words
    global inputs
    global inGame
    global statsDisplayer
    if inGame:
        statsDisplayer.updateStats(0, 0)
    inGame = True
    statsDisplayer.setMode(mode)
    if screen != None:
        screen.end()
        screen = None
    if mode == 0:
        word = all_words.getRandom()
        screen = Screen(canvas, window, gameOver, False, word, 6)
    elif mode == 1:
        word = all_words.getRandom()
        screen = Screen(canvas, window, gameOver, True, word, 6)
    elif mode == 2:
        ws = WordSearch(16,16)
        ws.genWordSearch()
        print(ws.getTarget())
        screen = WSGUI(ws, inputs, canvas, window, gameOver, False)
        screen.start()
    else:
        ws = WordSearch(16,16)
        ws.genWordSearch()
        print(ws.getTarget())
        screen = WSGUI(ws, inputs, canvas, window, gameOver, True)
        screen.start()

"""
sets mode
0: wordle
1: wordle hard mode
2: wordlesearch
3: wordlesearch hard mode
"""
def setmode(m):
    global mode
    mode = m

#main function to start gui
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
    
    displaySettings = SettingsDisplay(canvas, window, inputs, setmode, start, stop)
    statsDisplayer = StatsDisplayer(canvas, window, inputs, start, stop, "uwu", 6)

    canvas.create_rectangle(0,0,100,50,outline = "", fill = "orange")
    newGameButton = button.Button(inputs, window, newgame, 0, 0, 100, 50)
    newGameText = canvas.create_text(50, 25, anchor = CENTER)
    canvas.itemconfig(newGameText, text = "New Game", font = ("DIN Condensed", 30, "bold"), fill = "blue")

    newgame()
    window.mainloop()
actualgame()