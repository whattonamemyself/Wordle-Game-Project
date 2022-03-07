from tkinter import *
from button import Button
from inputwrapper import InputWrapper
from gui import Screen
from wordsearchgui import WSGUI


class SettingsDisplay:
    def __init__(self, canvas, window, inputs, screen):
        self.screen = screen
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
        if isinstance(self.screen, Screen):
            self.screen.pauseGame()
        elif isinstance(self.screen, WSGUI):
            self.screen.stop()
        settingsWidgets = []
        settingsWidgets.append(self.canvas.create_rectangle(0, 600, 1000, 0, fill = "black"))
        settingsWidgets.append(self.canvas.create_text(500,30, anchor = CENTER))
        self.canvas.itemconfig(settingsWidgets[1], text="Settings",font = ("DIN Condensed", 35, "bold"), fill = "white")
        
    def quitSettings(self, mode):
        if mode == None:
            if isinstance(self.screen, Screen):
                self.screen.resumeGame()
            elif isinstance(self.screen, WSGUI):
                self.screen.start()