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
    def __init__(self, canvas, window, inputs, name, maxtries = 6): #tk.canvas, tk.window, string, int
        self.canvas = canvas
        self.canvasitems = []
        self.window = window
        self.inputs = inputs
        self.wordleplayer = WordlePlayer(name, maxtries)
        self.wordlesearch = WordlePlayer(name, maxtries)
        self.button = Button(inputs, window, self.open, 800,50,900,150)
        self.closebutton = None
        self.bg = None
        self.tick = None
        self.active = False
        self.canvas.create_rectangle(800,50,900,150,fill="red")

    def roundrect(self, x1, y1, x2, y2, col = "red", rad=20):
        self.canvasitems.append(self.canvas.create_rectangle(x1+rad, y1, x2-rad, y2, fill=col, outline = ""))
        self.canvasitems.append(self.canvas.create_rectangle(x1, y1+rad, x2, y2-rad, fill=col, outline = ""))
        self.canvasitems.append(self.canvas.create_oval(x1, y1, x1+rad*2, y1+rad*2, fill=col, outline = ""))
        self.canvasitems.append(self.canvas.create_oval(x1, y2-rad*2, x1+rad*2, y2, fill=col, outline = ""))
        self.canvasitems.append(self.canvas.create_oval(x2-rad*2, y1, x2, y1+rad*2, fill=col, outline = ""))
        self.canvasitems.append(self.canvas.create_oval(x2-rad*2, y2-rad*2, x2, y2, fill=col, outline = ""))
    def open(self):
        self.closebutton = Button(self.inputs, self.window, self.close, 100,50,200,150)
        text = self.canvas.create_text(650,100, anchor = tk.NW)
        self.canvas.itemconfig(text, text="x",font = "Courier 80", fill = "black")

        self.bg = [300,100,700,500]
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

    def loop(self):
        if self.active:
            for item in self.canvasitems:
                self.canvas.delete(item)
            self.roundrect(self.bg[0],self.bg[1],self.bg[2],self.bg[3],col="red")
            self.tick += 1
            self.window.after(16, self.loop)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    inputs = InputWrapper(canvas)
    stats = StatsDisplayer(canvas, window, inputs, "mark", 6)
    window.mainloop()
if __name__ == "__main__":
    main()
