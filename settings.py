# imports
from tkinter import *
from button import Button
from gui import Screen
from wordsearchgui import WSGUI

# when instance of SettingsDisplay is made, it displays the button for settings
class SettingsDisplay:
    '''
    canvas -> tkinter canvas
    window -> tkinter window
    inputs -> input wrapper, can detect movements and key presses
    setmode -> function which sets the current mode
    start -> function which lets other widgets on screen be interacted with
    stop -> function which stops other widgets on screen from being interacted with
    '''
    def __init__(self, canvas, window, inputs, setmode, start, stop):
        self.start2 = start
        self.stop2 = stop
        self.settingsPaused = False
        self.setmode = setmode
        self.canvas = canvas
        self.window = window
        self.inputs = inputs
        self.tl = (800, 10)
        self.br = (850, 40)
        self.settings = Button(self.inputs, self.window, self.settingsPressed, self.tl[0], self.tl[1], self.br[0], self.br[1])
        x = self.tl[0]+(self.br[0]-self.tl[0])/2
        y = self.tl[1]+(self.br[1]-self.tl[1])/2
        self.canvas.create_text((x, y), text = "⚙", font = ("DIN Condensed", 50, "bold"), fill = "white")

    # stops settings button from opening
    def stop(self):
        self.settingsPaused = True

    # lets settings button be opened
    def start(self):
        self.settingsPaused = False

    # called when settings button is pressed, displays list of modes available
    def settingsPressed(self):
        if self.settingsPaused:
            return
        self.stop2()
        self.settingsWidgets = []
        self.settingsButtons = []
        self.settingsWidgets.append(self.canvas.create_rectangle(0, 600, 1000, 0, fill = "black"))
        self.settingsWidgets.append(self.canvas.create_text(500,30, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text="Settings",font = ("DIN Condensed", 35, "bold"), fill = "white")

        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings("normal"), 150, 150, 300, 200))
        self.settingsWidgets.append(self.canvas.create_rectangle(150, 150, 300, 200, fill = "#848484"))
        self.settingsWidgets.append(self.canvas.create_text(225, 175, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Normal Mode", font = ("DIN Condensed", 30, "bold"), fill = "white")

        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings("hard"), 150, 250, 300, 300))
        self.settingsWidgets.append(self.canvas.create_rectangle(150, 250, 300, 300, fill = "#848484"))
        self.settingsWidgets.append(self.canvas.create_text(225, 275, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Hard Mode", font = ("DIN Condensed", 30, "bold"), fill = "white")

        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings("ws"), 700, 150, 850, 200))
        self.settingsWidgets.append(self.canvas.create_rectangle(700, 150, 850, 200, fill = "#848484"))
        self.settingsWidgets.append(self.canvas.create_text(775, 175, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Wordle Wordsearch", font = ("DIN Condensed", 20, "bold"), fill = "white")

        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings("wshard"), 700, 250, 850, 300))
        self.settingsWidgets.append(self.canvas.create_rectangle(700, 250, 850, 300, fill = "#848484"))
        self.settingsWidgets.append(self.canvas.create_text(775, 275, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Wordle Wordsearch Hard Mode", font = ("DIN Condensed", 14, "bold"), fill = "white")

        self.settingsButtons.append(Button(self.inputs, self.window, lambda: self.quitSettings(None), 25, 25, 125, 75))
        self.settingsWidgets.append(self.canvas.create_rectangle(25, 25, 125, 75, fill = "red"))
        self.settingsWidgets.append(self.canvas.create_text(75, 50, anchor = CENTER))
        self.canvas.itemconfig(self.settingsWidgets[-1], text = "Back", font = ("DIN Condensed", 30, "bold"), fill = "white")

    # called when mode in settings is pressed, adjusts current mode accordingly
    def quitSettings(self, mode):
        self.start2()
        for i in self.settingsWidgets:
            self.canvas.delete(i)
        for i in self.settingsButtons:
            i.stop()
            del i
        if mode == "normal":
            self.setmode(0)
        elif mode == "hard":
            self.setmode(1)
        elif mode == "ws":
            self.setmode(2)
        elif mode == "wshard":
            self.setmode(3)
