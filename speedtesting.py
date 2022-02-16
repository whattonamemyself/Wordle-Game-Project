from tkinter import *
import random
from inputwrapper import InputWrapper

#ironically, this is the most efficient way to render stuff in tkinter that i know of :dead:
window = Tk()
canvas = Canvas(width = 800, height = 600)
thing = [None] * 100
uwu = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
inputs = InputWrapper(canvas)
def uwus():
    global uwu
    canvas.delete("all")
    txt = []
    uwu2 = list(uwu)
    random.seed(1)
    for i in range(50):
        txt.append(" ")
        for x in range(99):
            txt.append(uwu2[(x)%len(uwu2)])
        txt.append('\n')
    txt2 = "".join(txt)
    canvas.create_text(0,0,fill="darkblue",font=("Courier",10),text=txt2,anchor=NW)
    if not inputs.isMouseDown():
        uwu = uwu[1:]+uwu[:1]
    window.after(1, uwus)
canvas.pack()
uwus()
window.mainloop()