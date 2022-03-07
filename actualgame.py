from wordbank import WordBank
from gui import Screen
from tkinter import *
from wordsearchgui import WSGUI
from wordsearch import WordSearch
from inputwrapper import InputWrapper
from settings import SettingsDisplay

def actualgame():
    window = Tk()
    canvas = Canvas(window, width = 1000, height = 600, bg = "black")
    canvas.pack()
    all_words = WordBank("common5letter.txt")
    inputs = InputWrapper(canvas)
    while True:
        word = all_words.getRandom()
        screen = Screen(canvas, window, False, word, 6)
        displaySettings = SettingsDisplay(canvas, window, inputs, screen)
        window.mainloop()
    # ws = WordSearch(20,20)
    # ws.genWordSearch()
    # gui = WSGUI(ws,inputs, canvas, window)
    # gui.update()
    # screen = Screen(canvas, window, False, word, 6)
    # print(screen.getGuess())
    # window.mainloop()   
actualgame()