from tkinter import *
from button import Button
from inputwrapper import InputWrapper
from gui import Screen
from wordsearchgui import WSGUI
from wordbank import WordBank


class SettingsDisplay:
    def __init__(self, canvas, window, inputs, screen, setmode):
        self.setmode = setmode
        self.screen = screen
        self.canvas = canvas
        self.window = window
        self.inputs = inputs
        self.tl = (800, 10)
        self.br = (850, 40)
        self.settings = Button(self.inputs, self.window, self.settingsPressed, self.tl[0], self.tl[1], self.br[0], self.br[1])
        x = self.tl[0]+(self.br[0]-self.tl[0])/2
        y = self.tl[1]+(self.br[1]-self.tl[1])/2
        self.canvas.create_text((x, y), text = "⚙", font = ("DIN Condensed", 50, "bold"), fill = "white")
    def settingsPressed(self):
        # if self.screen.transition: return
        if isinstance(self.screen, Screen):
            self.screen.pauseGame()
        elif isinstance(self.screen, WSGUI):
            self.screen.stop()
        self.settingsWidgets = []
        self.settingsButtons = []
        self.settingsWidgets.append(self.canvas.create_rectangle(0, 600, 1000, 0, fill = "black"))
        self.settingsWidgets.append(self.canvas.create_text(500,30, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text="Settings",font = ("DIN Condensed", 35, "bold"), fill = "white")
        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings("normal"), 200, 100, 500, 400))
        self.settingsWidgets.append(self.canvas.create_rectangle(150, 300, 200, 350, fill = "green"))
        self.settingsWidgets.append(self.canvas.create_text(175, 325, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Normal Mode", font = ("DIN Condensed", 30, "bold"), fill = "white")
    def quitSettings(self, mode):
        for i in self.settingsWidgets:
            self.canvas.delete(i)
        for i in self.settingsButtons:
            i.stop()
            del i
        if mode == None:
            if isinstance(self.screen, Screen):
                self.screen.resumeGame()
            elif isinstance(self.screen, WSGUI):
                self.screen.start()
        elif mode == "normal":
            self.setmode(0)
