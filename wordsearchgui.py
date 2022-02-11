import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper

class WSGUI():
    def __init__(self,ws,inputs,canvas, window):
        self.wordsearch = ws
        self.inputs = inputs
        self.canvas = canvas
        self.window = window
        w = self.wordsearch.getWidth()
        h = self.wordsearch.getHeight()
        self.hover = canvas.create_oval(0,0,10,10,fill='gray',outline = "")
        for x in range(w):
            for y in range(h):
                text = canvas.create_text((x+2) * 500 // w, 500-(y-1)*500//h, anchor = tk.CENTER)
                canvas.itemconfig(text, text=self.wordsearch.getGrid()[x][y],font = "Rubik 12 bold")

    def update(self):
        self.window.after(16, self.update)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    inputs = InputWrapper(canvas)
    wordsearch = ws.WordSearch(20,20)
    wordsearch.genWordSearch()

    wsgui = WSGUI(wordsearch, inputs, canvas, window)
    wsgui.update()
    print("HII")
    window.mainloop()
if __name__ == "__main__":
    main()
