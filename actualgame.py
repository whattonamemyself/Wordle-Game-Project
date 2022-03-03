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
    all_words = WordBank("words_alpha.txt")
    inputs = InputWrapper(canvas)
    displaySettings = SettingsDisplay(canvas, window, inputs)   
    mode = "normal"
    while True:
        if mode == "normal":
            word = all_words.getRandom()
            screen = Screen(canvas, window, False, word, 6)
            window.mainloop()
    # ws = WordSearch(20,20)
    # ws.genWordSearch()
    # gui = WSGUI(ws,inputs, canvas, window)
    # gui.update()
    # screen = Screen(canvas, window, False, word, 6)
    # print(screen.getGuess())
    # window.mainloop()   
actualgame()