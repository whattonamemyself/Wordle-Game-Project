import tkinter as tk
import wordsearch as ws
from inputwrapper import InputWrapper
from wordleword import WordleWord
from wordbank import WordBank
from markguess import markGuess
from confettiuwu import Confetti
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
        self.confetti = Confetti(self.canvas, self.window)
        self.active = False
        w = self.wordsearch.getWidth()
        h = self.wordsearch.getHeight()
        self.hoverPos = [0,0]
        for x in range(w):
            for y in range(h):
                p = self.getPos2(x, y)
                text = canvas.create_text(p[0], p[1], anchor = tk.CENTER)
                canvas.itemconfig(text, text=self.wordsearch.getGrid()[x][y],font = "Rubik 12 bold", fill = "black")
    def getPos(self, x, y):
        h = self.wordsearch.getHeight()
        return [round((x - 75)/30), round((h * 30 - y + 50)/30)]
    def getPos2(self, x, y):
        h = self.wordsearch.getHeight()
        return [x * 30 + 75, h * 30 - y * 30 + 50]
    
    def inside(self, x, y, x1, y1, x2, y2):
        return x >= x1 and x <= x2 and y >= y1 and y <= y2

    def renderHL(self, hl, col = "#69D420"):
            tmp = self.canvas.create_line(hl[0],hl[1],hl[2],hl[3], width = 30, fill = col)
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(hl[0]-15,hl[1]-15,hl[0]+15,hl[1]+15, fill = col, outline = "")
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)
            tmp = self.canvas.create_oval(hl[2]-15,hl[3]-15,hl[2]+15,hl[3]+15, fill = col, outline = "")
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)

    def manageGuesses(self): # deals with the guesses
        text = self.canvas.create_text(919,69, anchor = tk.NW)
        self.canvas.itemconfig(text, text="☑",font = "Courier 80", fill = "black") #renders checkmark
        self.canvasItems.append(text)
        if len(self.curGuess) >= 3: # yes current guess
            tmp = self.canvas.create_rectangle(925,95,960,130, outline = "", fill = "#00cc42")
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)
            
            if self.inputs.isMouseDown() and not self.mouseWasDown: 
                if self.inside(self.inputs.getMouseX(), self.inputs.getMouseY(), 925, 95, 960, 130): # button pressed!
                    if self.wordlist.contains(self.curGuess): #word is a valid word
                        uwu = WordleWord(self.curGuess) 
                        correct = self.wordsearch.target == self.curGuess
                        markGuess(self.wordsearch.target, uwu, self.alpha) 
                        self.guesses.append(WordDisplayer(uwu, (575, len(self.guesses) * 35 + 230))) 
                        self.curGuess = ""
                        self.guesshl.append(self.curHL)
                        self.curHL = None
                        if correct == 1: # word is correct
                            self.confetti.__init__(self.canvas, self.window)
                            self.window.after(0,self.confetti.update)
                            pass #TODO - return win + guesses | return len(self.guesses) | stop
                        elif len(self.guesses) == 6:
                            pass #TODO - return lose | return 7 | stop
                    else:
                        self.invalid = 800 #displays message saying word is invalid
        else: # no current guess
            tmp = self.canvas.create_rectangle(925,95,960,130, outline = "", fill = "#696969") 
            self.canvas.lower(tmp)
            self.canvasItems.append(tmp)

        if self.invalid > 0: #renders the red text telling you that you didnt enter a valid word
            text = self.canvas.create_text(575,140, anchor = tk.NW)
            gb = min(self.invalid, 255) # green and blue values
            col = hex(gb*256*256 + 0*256 + 0)[2:]
            while len(col)<6:
                col = '0' + col
            col = '#' + col
            self.canvas.itemconfig(text, text="Uh oh, it seems like your word DOESNT EXIST IDIOT",font = "Courier 14", fill = col) #renders checkmark
            self.canvasItems.append(text)
            self.invalid -= 8
        
        #render previous guesses
        text = self.canvas.create_text(575,190, anchor = tk.NW)
        self.canvas.itemconfig(text, text="Guesses: ",font = "Courier 36", fill = "white")
        self.canvasItems.append(text)
        for guess in self.guesses:
            guess.upd(self.canvas, self.canvasItems)
        for guess in self.guesshl:
            self.renderHL(guess, "#69F6F9")
        self.alphaDisplay.setWordleWord(self.alpha)
        self.alphaDisplay.upd(self.canvas, self.canvasItems)
    def start(self):
        self.active = True
        self.update()
    def stop(self):
        self.active = False
    def update(self): #updates every frame
        if self.active:
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
                self.renderHL(a+b, col="#696969")
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
                
            if self.isDragging or ((not self.inputs.isMouseDown()) and mousePos[0] >= 0 and mousePos[1] >= 0 and mousePos[0] < w and mousePos[1] < h): #highlight is on
                tmp = self.canvas.create_oval(self.hoverPos[0] - 15, self.hoverPos[1] - 15, self.hoverPos[0] + 15, self.hoverPos[1] + 15, fill = "#696969", outline = "")
                self.canvas.tag_lower(tmp)
                self.canvasItems.append(tmp)
            
            if not self.inputs.isMouseDown(): #not dragging
                self.isDragging = False
                self.mouseDownX = -1
                self.mousedownY = -1


            if not self.curHL == None and not self.isDragging:
                self.renderHL(self.curHL)

            if len(self.curGuess): #displays current text
                text = self.canvas.create_text(575,95, anchor = tk.NW)
                self.canvas.itemconfig(text, text=self.curGuess,font = "Courier 36", fill = "white")
                self.canvasItems.append(text)

            tmp = self.canvas.create_line(575,130,900,130,width = 2.718, fill = "#FFFFFF")
            self.canvasItems.append(tmp)

            self.manageGuesses()
            self.mouseWasDown = self.inputs.isMouseDown()
            self.window.after(16, self.update)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600, bg = "black")
    canvas.pack()
    inputs = InputWrapper(canvas)
    wordsearch = ws.WordSearch(15,15)
    wordsearch.genWordSearch()
    print(wordsearch.target)    
    wsgui = WSGUI(wordsearch, inputs, canvas, window)
    wsgui.start()
    print("HII")
    window.mainloop()
if __name__ == "__main__":
    main()
