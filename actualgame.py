from wordbank import WordBank
from gui import Screen
from tkinter import *
from wordsearchgui import WSGUI
from wordsearch import WordSearch
from inputwrapper import InputWrapper

window = Tk()
def actualgame():
    canvas = Canvas(window, width = 1000, height = 600, bg = "black")
    all_words = WordBank("words_alpha.txt")
    word = all_words.getRandom()
    ws = WordSearch(20,20)
    ws.genWordSearch()
    inputs = InputWrapper(canvas)
    gui = WSGUI(ws,inputs, canvas, window)
    gui.update()
    screen = Screen(canvas, window, False, word, 6)
    print(screen.getGuess())
    window.mainloop()   
actualgame()