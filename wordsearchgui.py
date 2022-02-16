import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper
from game import markGuess
direction = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1)
]
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
        self.curGuess = ""
        self.curHL = None
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
        return [round((x - 75)/30), round((h * 30 - y + 50)/30)]
    def getPos2(self, x, y):
        h = self.wordsearch.getHeight()
        return [x * 30 + 75, h * 30 - y * 30 + 50]
    
    def manageGuesses(self):
        if len(self.curGuess) >= 3:
            tmp = self.canvas.create_rectangle(930,75,955,110, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_rectangle(925,80,960,105, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(925,75,935,85, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(950,75,960,85, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(925,100,935,110, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(950,100,960,110, outline = "", fill = "#00cc42")
            self.canvasItems.append(tmp)
            text = self.canvas.create_text(928,79, anchor = tk.NW)
            self.canvas.itemconfig(text, text="✔️",font = "Courier 30", fill = "#FFFFFF")
            self.canvasItems.append(text)
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
            self.curHL = None
            self.curGuess = ""
            a = self.getPos2(self.mouseDownX, self.mouseDownY)
            b = self.hoverPos
            tmp = self.canvas.create_line(a[0],a[1],b[0],b[1], width = 30, fill = "#696969")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(a[0] - 15, a[1] - 15, a[0] + 15, a[1] + 15, fill = "#696969", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            c = mousePos2[0] - self.mouseDownX
            d = mousePos2[1] - self.mouseDownY
            if not (c == 0 and d == 0):
                l = max(abs(c),abs(d))
                e = [c/l,d/l]
                dir = -1
                for i, v in enumerate(direction):
                    if e[0] == v[0] and e[1] == v[1]:
                        dir = i
                if dir != -1:
                    self.curHL = [self.mouseDownX, self.mouseDownY, mousePos2[0], mousePos2[1]]
                    self.curHL[:2] = self.getPos2(self.curHL[0], self.curHL[1])
                    self.curHL[2:] = self.getPos2(self.curHL[2], self.curHL[3])
                    self.curGuess = self.wordsearch.getWord(self.mouseDownX, self.mouseDownY, dir, l + 1)
        
        
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


        if not self.curHL == None and not self.isDragging:
            tmp = self.canvas.create_line(self.curHL[0],self.curHL[1],self.curHL[2],self.curHL[3], width = 30, fill = "#69D420")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(self.curHL[0]-15,self.curHL[1]-15,self.curHL[0]+15,self.curHL[1]+15, fill = "#69D420", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(self.curHL[2]-15,self.curHL[3]-15,self.curHL[2]+15,self.curHL[3]+15, fill = "#69D420", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)

        if len(self.curGuess):
            text = self.canvas.create_text(575,75, anchor = tk.NW)
            self.canvas.itemconfig(text, text=self.curGuess,font = "Courier 36")
            self.canvasItems.append(text)
            tmp = self.canvas.create_line(575,110,575+22*len(self.curGuess),110,width = 2.718, fill = "#000000")
            self.canvasItems.append(tmp)

        self.manageGuesses()
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
