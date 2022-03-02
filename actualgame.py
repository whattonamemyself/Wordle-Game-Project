from wordbank import WordBank
from gui import Screen
from tkinter import *

def actualgame():
    window = Tk()
    canvas = Canvas(window, width = 1000, height = 600, bg = "black")
    all_words = WordBank("words_alpha.txt")
    word = all_words.getRandom()
    screen = Screen(canvas, window, False, word, 6)
    print(screen.getGuess())
actualgame()