class InputWrapper: #deals with all the input stuff
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

    def getMousePosition(self):
        return (self.mouseX, self.mouseY)

    def getMouseX(self):
        return self.mouseX

    def getMouseY(self):
        return self.mouseY

    def isMouseDown(self):
        return self.mouseDown

    def isKeyDown(self, key):
        if key in self.keys.keys(): #these are 2 different keys :dead:
            return self.keys[key]
        else:
            return False
