from wordleplayer import WordlePlayer
from inputwrapper import InputWrapper
from button import Button
import tkinter as tk
"""
def __init__(self, n, maxtries):
    super().__init__(n)
    self.won = 0
    self.games = 0
    self.streak = 0
    self.maxstreak = 0
    self.tries = [0] * maxtries 
"""
class StatsDisplayer:
    def __init__(self, canvas, window, inputs, start, stop, name, maxtries = 6): #tk.canvas, tk.window, string, int
        self.start = start
        self.stop = stop
        self.canvas = canvas
        self.maxtries = maxtries
        self.canvasitems = []
        self.window = window
        self.inputs = inputs
        self.wordleplayer = WordlePlayer(name, maxtries)
        self.wordlesearch = WordlePlayer(name, maxtries)
        self.button = Button(inputs, window, self.open, 950,0,1000,50)
        self.closebutton = None
        self.mode = 0
        self.bg = None
        self.tick = None
        self.active = False
        text = self.canvas.create_text(952,50, anchor = tk.NW)           
        self.canvas.itemconfig(text, text="📊",font = ("Courier", 50, "bold"), fill = "white")
        
    def setModeWordle(self):
        self.mode = 0
    def setModeWordleSearch(self):
        self.mode = 1
    def updateStats(self, win, tries):
        if self.mode == 0:
            self.wordleplayer.updateStats(win, tries)
        else:
            self.wordlesearch.updateStats(win, tries)
    def roundrect(self, x1, y1, x2, y2, col = "red", rad=20):
        res = []
        res.append(self.canvas.create_rectangle(x1+rad, y1, x2-rad, y2, fill=col, outline = ""))
        res.append(self.canvas.create_rectangle(x1, y1+rad, x2, y2-rad, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x1, y1, x1+rad*2, y1+rad*2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x1, y2-rad*2, x1+rad*2, y2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x2-rad*2, y1, x2, y1+rad*2, fill=col, outline = ""))
        res.append(self.canvas.create_oval(x2-rad*2, y2-rad*2, x2, y2, fill=col, outline = ""))
        return res
    def open(self):
        self.stop()
        if self.active:
            return
        self.closebutton = Button(self.inputs, self.window, self.close, 640,110,690,160)

        self.bg = [300,100,700,500]
        self.bars = [0] * self.maxtries

        self.tick = 0
        self.active = True
        self.loop()

    def close(self):
        if self.closebutton != None:
            self.closebutton.stop()
            del self.closebutton
        self.active = False
        for item in self.canvasitems:
            self.canvas.delete(item)
        self.start()

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
        if self.mode == 0:
            stats = self.wordleplayer
        else:
            stats = self.wordlesearch
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
            self.canvas.itemconfig(text, text=str(i),font = ("DIN Condensed", 20, "bold"), fill = "black")
            self.canvasitems.append(text)
            
            text = self.canvas.create_text(370 + self.bars[i]*3,i*40+245, anchor = tk.NW)           
            self.canvas.itemconfig(text, text=str(stats.tries[i]),font = ("DIN Condensed", 20, "bold"), fill = "black")
            self.canvasitems.append(text)

        self.tick += 1
        self.window.after(16, self.loop)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    inputs = InputWrapper(canvas)
    stats = StatsDisplayer(canvas, window, inputs, "mark", 6)
    stats.updateStats(1,1)
    stats.updateStats(1,2)
    stats.updateStats(1,2)
    stats.updateStats(1,3)
    window.mainloop()
if __name__ == "__main__":
    main()
