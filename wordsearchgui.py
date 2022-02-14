import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper

class WSGUI():
    def __init__(self,ws,inputs,canvas, window):
        self.wordsearch = ws
        self.inputs = inputs
        self.canvas = canvas
        self.window = window
        self.mouseDownX = -1
        self.mouseDownY = -1
        self.isDragging = False
        self.mouseWasDown = False
        self.canvasItems = []
        w = self.wordsearch.getWidth()
        h = self.wordsearch.getHeight()
        self.hoverPos = [0,0]
        for x in range(w):
            for y in range(h):
                p = self.getPos2(x, y)
                text = canvas.create_text(p[0], p[1], anchor = tk.CENTER)
                canvas.itemconfig(text, text=self.wordsearch.getGrid()[x][y],font = "Rubik 12 bold")
    def getPos(self, x, y):
        h = self.wordsearch.getHeight()
        return [round((x - 50)/26), round((h * 26 - y + 24)/26)]
    def getPos2(self, x, y):
        h = self.wordsearch.getHeight()
        return [x * 26 + 50, h * 26 - y * 26 + 24]
    def update(self):
        for x in self.canvasItems:
            self.canvas.delete(x)
        self.canvasItems = []
        w = self.wordsearch.getHeight()
        h = self.wordsearch.getHeight()

        mousePos = self.getPos(self.inputs.getMouseX(), self.inputs.getMouseY())
        mousePos2 = mousePos[:]
        if mousePos2[0] < 0: mousePos2[0] = 0
        if mousePos2[1] < 0: mousePos2[1] = 0
        if mousePos2[0] >= w: mousePos2[0] = w-1
        if mousePos2[1] >= h: mousePos2[1] = h-1
        target = self.getPos2(mousePos2[0], mousePos2[1])
        speed = 3.1415926535897932384626533
        self.hoverPos[0] += (target[0] - self.hoverPos[0]) / speed
        self.hoverPos[1] += (target[1] - self.hoverPos[1]) / speed

        if self.isDragging:
            a = self.getPos2(self.mouseDownX, self.mouseDownY)
            b = self.hoverPos
            tmp = self.canvas.create_line(a[0],a[1],b[0],b[1], width = 31, fill = "#696969")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(a[0] - 15, a[1] - 15, a[0] + 15, a[1] + 15, fill = "#696969", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)

        if self.inputs.isMouseDown() and (not self.mouseWasDown) and mousePos[0] >= 0 and mousePos[1] >= 0 and mousePos[0] < w and mousePos[1] < h:
            self.isDragging = True
            self.mouseDownX = mousePos[0]
            self.mouseDownY = mousePos[1]
            
        if self.isDragging or ((not self.inputs.isMouseDown()) and mousePos[0] >= 0 and mousePos[1] >= 0 and mousePos[0] < w and mousePos[1] < h):
            tmp = self.canvas.create_oval(self.hoverPos[0] - 15, self.hoverPos[1] - 15, self.hoverPos[0] + 15, self.hoverPos[1] + 15, fill = "#696969", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
        
        if not self.inputs.isMouseDown():
            self.isDragging = False
            self.mouseDownX = -1
            self.mousedownY = -1
        self.mouseWasDown = self.inputs.isMouseDown()
        self.window.after(16, self.update)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    inputs = InputWrapper(canvas)
    wordsearch = ws.WordSearch(15,15)
    wordsearch.genWordSearch()
    print(wordsearch.target)    
    wsgui = WSGUI(wordsearch, inputs, canvas, window)
    wsgui.update()
    print("HII")
    window.mainloop()
if __name__ == "__main__":
    main()
