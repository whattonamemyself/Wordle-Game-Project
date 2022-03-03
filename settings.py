from tkinter import *
from button import Button
from PIL import ImageTk,Image  


class SettingsDisplay:
    def __init__(self, canvas, window, inputs):
        self.canvas = canvas
        self.window = window
        self.inputs = inputs
        self.currDisplay = False
        self.tl = (800, 10)
        self.br = (850, 40)
        settings = Button(inputs, window, self.settingsPressed, self.tl[0], self.tl[1], self.br[0], self.br[1])
        settingsPic = PhotoImage(file="settingspic.png")
        self.canvas.create_image(100,100, anchor=NW, image=settingsPic) 
        self.canvas.create_rectangle(self.tl[0], self.tl[1], self.br[0], self.br[1], fill = "green")
    def settingsPressed(self):
        if not self.currDisplay:
            self.currDisplay = True
        else:
            self.currDisplay = False
        print("ALSKJGAKSDJG;AKSFK")
# window = Tk()
# canvas = Canvas(window, width = 1000, height = 600, bg = "black")
# inputs = InputWrapper(canvas)
# displaySettings = SettingsDisplay(canvas, window, inputs)   
# window.mainloop()