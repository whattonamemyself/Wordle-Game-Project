
class Button:
    def __init__(self, inputs, window, func, x1, y1, x2, y2):
        self.inputs = inputs
        self.window = window
        self.mouseWasDown = False
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.func = func
        self.loop()
    def inside(self, x, y, x1, y1, x2, y2):
        return x >= x1 and x <= x2 and y >= y1 and y <= y2
    def loop(self):
        if self.inputs.isMouseDown() and not self.mouseWasDown: 
            if self.inside(self.inputs.getMouseX(), self.inputs.getMouseY(), self.x1, self.y1, self.x2, self.y2):
                self.func()
        self.mouseWasDown = self.inputs.isMouseDown()
        self.window.after(16, self.loop)