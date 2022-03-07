from tkinter import *
from button import Button
from inputwrapper import InputWrapper
import random


class SettingsDisplay:
    def __init__(self, canvas, window, inputs):
        self.canvas = canvas
        self.window = window
        self.inputs = inputs
        self.tl = (800, 10)
        self.br = (850, 40)
        self.settings = Button(inputs, window, self.settingsPressed, self.tl[0], self.tl[1], self.br[0], self.br[1])
        x = self.tl[0]+(self.br[0]-self.tl[0])/2
        y = self.tl[1]+(self.br[1]-self.tl[1])/2
        self.canvas.create_text((x, y), text = "⚙", font = ("DIN Condensed", 50, "bold"), fill = "white")
    def settingsPressed(self):
        self.canvas.create_rectangle(0, 600, 1000, 0, fill = "#"+str(random.randint(0,3))+"c3c3c")