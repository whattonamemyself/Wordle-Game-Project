#deals with all the input stuff
class InputWrapper: 
    def __init__(self, canvas):
        self.keys = {}
        self.mouseDown = False
        self.mouseX = -1000
        self.mouseY = -1000
        canvas.bind_all('<KeyPress>',self.keyPressed)
        canvas.bind_all('<KeyRelease>',self.keyReleased)
        canvas.bind_all('<ButtonPress-1>',self.mousePressed)
        canvas.bind_all('<ButtonRelease-1>',self.mouseReleased)
        canvas.bind_all('<Motion>',self.motion)
    
    #tkinter api start
    def motion(self, e):
        self.mouseX, self.mouseY = e.x, e.y

    def mousePressed(self, e):
        self.mouseDown = True

    def mouseReleased(self, e):
        self.mouseDown = False

    def keyPressed(self, e):
        self.keys[e.char] = True

    def keyReleased(self, e):
        self.keys[e.char] = False
    #tkinter api end

    #gets mouse position, returns tuple(int,int)
    def getMousePosition(self):
        return (self.mouseX, self.mouseY)

    #gets mouse x, returns int
    def getMouseX(self):
        return self.mouseX

    #gets mouse y, returns int
    def getMouseY(self):
        return self.mouseY

    #returns true if mouse is down, false if not (bool)
    def isMouseDown(self):
        return self.mouseDown

    #returns true if the key is down, false if not (bool)
    def isKeyDown(self, key):
        if key in self.keys.keys():
            return self.keys[key]
        else:
            return False
