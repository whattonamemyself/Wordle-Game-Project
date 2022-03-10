# when instance of Button is made, a new button can be made
class Button:
    '''
    inputs -> InputWrapper, detects key presses and mouse movements
    window -> tkinter window
    func -> called when button is pressed
    x1 -> top left x coord
    x2 -> bottom right y coord
    y1 -> top left x coord
    y2 -> bottom right y coord
    '''
    def __init__(self, inputs, window, func, x1, y1, x2, y2):
        self.inputs = inputs
        self.window = window
        self.mouseWasDown = False
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.func = func
        self.active = True
        self.loop()
    # turns off button, call before deleting class
    def stop(self):
        self.active = False
    # called to see if mouse press is inside button region
    def inside(self, x, y, x1, y1, x2, y2):
        return x >= x1 and x <= x2 and y >= y1 and y <= y2
    # updates the button every frame, button detects whether it is clicked or not
    def loop(self):
        if self.active:
            if self.inputs.isMouseDown() and not self.mouseWasDown: 
                if self.inside(self.inputs.getMouseX(), self.inputs.getMouseY(), self.x1, self.y1, self.x2, self.y2):
                    self.func()
            self.mouseWasDown = self.inputs.isMouseDown()
            self.window.after(16, self.loop)