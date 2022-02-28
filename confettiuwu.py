import tkinter as tk
import random
import math

def renderShape(canvas, canvasitems, numpoints, size, rot, xpos, ypos, ghost, col):
    points = []
    angle = rot/360*2*math.pi
    for i in range(numpoints):
        points.append(math.cos(angle)*size)
        points.append(math.sin(angle)*size)
        angle += 2*math.pi / numpoints
    for i in range(numpoints):
        points[i*2] += xpos
        points[i*2+1] += ypos
    
    
    gh = min(ghost, 255)/255
    r = round(col[0]*(gh) + 255 * (1-gh))
    g = round(col[0]*(gh) + 255 * (1-gh))
    b = round(col[0]*(gh) + 255 * (1-gh))
    col = hex(r*256*256 + g*256 + b)[2:]
    while len(col) < 6:
        col = '0' + col
    col = '#' + col
    shape = canvas.create_polygon(points,outline = "", fill = col, width = 0)
    canvasitems.append(shape)
class Confetti():
    def __init__(self,canvas, window):
        self.canvas = canvas
        self.window = window
        self.canvasitems = []
        self.shape = []
        self.size = []
        self.rot = []
        self.xpos = []
        self.ypos = []
        self.yv = []
        self.xv = []
        self.tick = 0
        self.delay = []
        self.ghost = []
        self.col = []
        for i in range(200):
            self.delay.append(random.randint(1,50))
            self.ghost.append(400)
            force = random.random() * 1.25
            self.shape.append(random.randint(0,2))
            self.size.append(random.randint(5,10))
            self.rot.append(random.randint(0,360))
            self.yv.append(random.random()*-20 + force * -5 - 10)
            self.ypos.append(600)
            self.col.append((random.randint(0,1)*255, random.randint(0,1)*255, random.randint(0,1)*255))
            if random.randint(0,1) == 0:
                self.xpos.append(0)
                self.xv.append(random.random()*15 + force * 10)
            else:
                self.xpos.append(1000)
                self.xv.append(random.random()*-15 + force * -10)

    def update(self): #updates every frame
        for i in self.canvasitems:
            self.canvas.delete(i)
        if self.tick > 20:
            for i in range(200):
                if self.delay[i] < self.tick :
                    self.xpos[i] += self.xv[i]
                    self.ypos[i] += self.yv[i]
                    self.yv[i] += 1
                    self.xv[i] *= 0.95
                    self.ghost[i] -= 10
                    if self.ghost[i] > 0:
                        renderShape(self.canvas, self.canvasitems, self.shape[i] + 3, self.size[i], self.rot[i], self.xpos[i], self.ypos[i], self.ghost[i], self.col[i])
        self.tick += 1
        self.window.after(16, self.update)

def main():
    window = tk.Tk()
    canvas = tk.Canvas(width = 1000, height = 600)
    canvas.pack()
    confetti = Confetti(canvas, window)
    confetti.update()
    window.mainloop()
if __name__ == "__main__":
    main()
