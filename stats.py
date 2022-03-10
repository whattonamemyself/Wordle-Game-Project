from wordleplayer import WordlePlayer
from inputwrapper import InputWrapper
from button import Button
import tkinter as tk

#class StatsDisplayer: creates a button that, when clicked, opens a window that displays the stats
class StatsDisplayer:
    """
    Initializer
    inputs: Tkinter Canvas, Tkinter Window, InputWrapper, Function, Function, String, Int
    stop: function that this class calls to pause all other classes
    start: function that this class calls to unpause all other classes
    name: name? apparently its not used
    maxtries: maximum number of tries
    """
    def __init__(self, canvas, window, inputs, start, stop, name, maxtries = 6): #tk.canvas, tk.window, string, int
        self.start2 = start
        self.stop2 = stop
        self.canvas = canvas
        self.maxtries = maxtries
        self.canvasitems = []
        self.window = window
        self.inputs = inputs
        self.wordleplayer = [None] * 4
        for i in range(4):
            self.wordleplayer[i] = WordlePlayer(1,6)
        self.button = Button(inputs, window, self.open, 950,0,1000,50)
        self.closebutton = None
        self.mode = 0
        self.bg = None
        self.tick = None
        self.active = False
        self.buttonPaused = False
        text = self.canvas.create_text(950,5, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="📊",font = ("Courier", 50, "bold"), fill = "white")
    #stop: pauses the class
    def stop(self):
        self.buttonPaused = True
    #start: starts the class
    def start(self):
        self.buttonPaused = False
    #setmode: set the gamemode - different statistics for different modes
    def setMode(self, mode):
        self.mode = mode
    """
    updateStats:
    inputs: bool, Int
    win - did you win?
    tries - number of tries
    """
    def updateStats(self, win, tries):
        self.wordleplayer[self.mode].updateStats(win, tries)
    #roundrect: creates a rounded rectangle
    #inputs: int,int,int,int,string,int
    def roundrect(self, x1, y1, x2, y2, col = "red", rad=20):
        res = []
        res.append(self.canvas.create_rectangle(x1+rad, y1, x2-rad, y2, fill=col, outline = ""))
        res.append(self.canvas.create_rectangle(x1, y1+rad, x2, y2-rad, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x1, y1, x1+rad*2, y1+rad*2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x1, y2-rad*2, x1+rad*2, y2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x2-rad*2, y1, x2, y1+rad*2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x2-rad*2, y2-rad*2, x2, y2, fill=col, outline = ""))
        return res
    #open: opens the window
    def open(self):
        if self.buttonPaused:
            return
        self.stop2()
        if self.active:
            return
        self.closebutton = Button(self.inputs, self.window, self.close, 640,110,690,160)

        self.bg = [300,100,700,500]
        self.bars = [0] * self.maxtries

        self.tick = 0
        self.active = True
        self.loop()
    #close: closes the window
    def close(self):
        if self.closebutton != None:
            self.closebutton.stop()
            del self.closebutton
        self.active = False
        for item in self.canvasitems:
            self.canvas.delete(item)
        self.start2()
    #loop: window loop, updates the window and renders it every frame
    def loop(self):
        if not self.active:
            return
        for item in self.canvasitems:
            self.canvas.delete(item)
        bg = self.roundrect(self.bg[0],self.bg[1],self.bg[2],self.bg[3],col="white")
        for i in range(len(bg)):
            self.canvasitems.append(bg[i])

        #x button
        text = self.canvas.create_text(640,90, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="x",font = ("Courier", 80, "bold"), fill = "black")
        self.canvasitems.append(text)

        #display stats
        stats = self.wordleplayer[self.mode]
        #text
        text = self.canvas.create_text(350,120, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="Games Played: "+str(stats.gamesPlayed()),font = ("DIN Condensed", 20, "bold"), fill = "black")
        self.canvasitems.append(text)
        text = self.canvas.create_text(350,140, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="Win %: "+ str(round(stats.winPercentage()))+'%',font = ("DIN Condensed", 20, "bold"), fill = "black")
        self.canvasitems.append(text)
        text = self.canvas.create_text(350,160, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="Current Streak: "+str(stats.currentStreak()),font = ("DIN Condensed", 20, "bold"), fill = "black")
        self.canvasitems.append(text)
        text = self.canvas.create_text(350,180, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="Max Streak: "+str(stats.maxStreak()),font = ("DIN Condensed", 20, "bold"), fill = "black")
        self.canvasitems.append(text)
        text = self.canvas.create_text(350,200, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="Guess Distribution",font = ("DIN Condensed", 20, "bold"), fill = "black")
        self.canvasitems.append(text)
        #bars
        tries = stats.getTries()
        for i in range(self.maxtries):
            self.bars[i] += (tries[i] - self.bars[i])/5
            bar = self.canvas.create_rectangle(350, i*40 + 240 , 350 + self.bars[i]*3, i*40 + 270, outline = "", fill = "green")
            self.canvasitems.append(bar)

            text = self.canvas.create_text(330,i*40+245, anchor = tk.NW)           
            self.canvas.itemconfig(text, text=str(i+1),font = ("DIN Condensed", 20, "bold"), fill = "black")
            self.canvasitems.append(text)
            
            text = self.canvas.create_text(370 + self.bars[i]*3,i*40+245, anchor = tk.NW)           
            self.canvas.itemconfig(text, text=str(stats.tries[i]),font = ("DIN Condensed", 20, "bold"), fill = "black")
            self.canvasitems.append(text)

        self.tick += 1
        self.window.after(16, self.loop)
