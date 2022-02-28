import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper
from wordleword import WordleWord
from wordbank import WordBank
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
class WordDisplayer:
    def __init__(self, wordleWord, pos):
        self.wordleWord = wordleWord
        self.p = pos
        self.pos = [None] * len(wordleWord.getWord())
        self.vel = [0] * len(wordleWord.getWord())
        self.sz = [0] * len(wordleWord.getWord())
        self.const = 20 # constant spacing
        self.tick = 0 # counts frames to to control duration
        for i in range(len(self.pos)):
            self.pos[i] = [self.p[0] + ((len(self.pos) - 1) / 2) * self.const, pos[1]]
    #assumes that the size of the input is the same as the size of the original word uwu
    def setWordleWord(self, wordleword): 
        uwu = wordleword
        #self.wordleword = wordleword
    def upd(self, canvas, canvasItems):
        for i in range(len(self.pos)):
            if self.tick > i:  
                self.pos[i][0] += (self.p[0] + i * self.const - self.pos[i][0]) / 5
                self.vel[i] += (36 - self.sz[i]) / 10
                self.vel[i] *= 0.8
                self.sz[i] += self.vel[i]
            if self.tick - i > 40:
                self.sz[i] = 36
            if self.sz[i] <= 3:
                continue
            text = canvas.create_text(self.pos[i][0],self.pos[i][1], anchor = tk.NW)
            if self.wordleWord.colorAt(i) == "normal":
                canvas.itemconfig(text, text=self.wordleWord.charAt(i),font = "Courier " + str(int(self.sz[i])), fill = "gray")
            else:
                canvas.itemconfig(text, text=self.wordleWord.charAt(i),font = "Courier " + str(int(self.sz[i])), fill = self.wordleWord.colorAt(i))
            canvasItems.append(text)
        self.tick += 1
class WSGUI():
    def __init__(self,ws,inputs,canvas, window):
        self.wordsearch = ws
        self.inputs = inputs
        self.canvas = canvas
        self.window = window
        self.wordlist = WordBank("words_alpha.txt") # word list
        self.mouseDownX = -1
        self.mouseDownY = -1
        self.isDragging = False
        self.mouseWasDown = False
        self.canvasItems = [] # list of all canvas items so i can delete them to update them every frame
        self.curGuess = "" # current guess
        self.guesses = [] # all guesses
        self.guesshl = [] # highlights guesses
        self.curHL = None # current highlight
        self.invalid = 0 # ghost effect of text "guess is invalid"
        self.alpha = WordleWord("abcdefghijklmnopqrstuvwxyz") #alphabet
        self.alphaDisplay = WordDisplayer(self.alpha, (66, 536))
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
    
    def inside(self, x, y, x1, y1, x2, y2):
        return x >= x1 and x <= x2 and y >= y1 and y <= y2

    def manageGuesses(self): # deals with the guesses
        text = self.canvas.create_text(919,69, anchor = tk.NW)
        self.canvas.itemconfig(text, text="☑",font = "Courier 80", fill = "white") #renders checkmark
        self.canvasItems.append(text)
        if len(self.curGuess) >= 3: # yes current guess
            tmp = self.canvas.create_rectangle(925,95,960,130, outline = "", fill = "#00cc42")
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)
            
            if self.inputs.isMouseDown() and not self.mouseWasDown: 
                if self.inside(self.inputs.getMouseX(), self.inputs.getMouseY(), 925, 95, 960, 130): # mouse clicked the check mark
                    if self.wordlist.contains(self.curGuess): #check if word in wordlist
                        uwu = WordleWord(self.curGuess) 
                        correct = markGuess(self.wordsearch.target, uwu, self.alpha) #marks guess
                        self.guesses.append(WordDisplayer(uwu, (575, len(self.guesses) * 35 + 230))) # renders guess
                        self.curGuess = ""
                        self.curHL = None
                        if correct == 1:
                            pass # solved
                    else:
                        self.invalid = 800
        else: # no current guess
            tmp = self.canvas.create_rectangle(925,95,960,130, outline = "", fill = "#696969") 
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)

        if self.invalid > 0: #renders the red text telling you that you didnt enter a valid word
            text = self.canvas.create_text(575,140, anchor = tk.NW)
            gb = 255-min(self.invalid, 255) # green and blue values
            col = '#' + hex(255*256*256 + gb*256 + gb)[2:]
            self.canvas.itemconfig(text, text="Uh oh, it seems like your word DOESNT EXIST IDIOT",font = "Courier 14", fill = col) #renders checkmark
            self.canvasItems.append(text)
            self.invalid -= 8

        
        text = self.canvas.create_text(575,190, anchor = tk.NW)
        self.canvas.itemconfig(text, text="Guesses: ",font = "Courier 36")
        self.canvasItems.append(text)
        for guess in self.guesses:
            guess.upd(self.canvas, self.canvasItems)
        self.alphaDisplay.setWordleWord(self.alpha)
        self.alphaDisplay.upd(self.canvas, self.canvasItems)

    def update(self): #updates every frame
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


        if self.isDragging: # creates the gray marker
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
                if l >= 2:
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


        if not self.curHL == None and not self.isDragging: #renders gray marker
            tmp = self.canvas.create_line(self.curHL[0],self.curHL[1],self.curHL[2],self.curHL[3], width = 30, fill = "#69D420")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(self.curHL[0]-15,self.curHL[1]-15,self.curHL[0]+15,self.curHL[1]+15, fill = "#69D420", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(self.curHL[2]-15,self.curHL[3]-15,self.curHL[2]+15,self.curHL[3]+15, fill = "#69D420", outline = "")
            self.canvas.tag_lower(tmp)
            self.canvasItems.append(tmp)

        if len(self.curGuess): #displays current text
            text = self.canvas.create_text(575,95, anchor = tk.NW)
            self.canvas.itemconfig(text, text=self.curGuess,font = "Courier 36")
            self.canvasItems.append(text)

        tmp = self.canvas.create_line(575,130,900,130,width = 2.718, fill = "#000000")
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
