'''
Platformer Game
By Eric
-----------------
Arrow keys to move.
Do not touch red
Black is platform
Yellow is bouncy
'''
from tkinter import *
window = Tk()
canvas = Canvas(window, width=1000, height = 600)
canvas.pack()
a = canvas.create_rectangle(0,0,40,40,fill = 'red')#player
def recreate():#recreates player
    global a
    canvas.delete(a)
    a = canvas.create_rectangle(0,0,40,40,fill = 'blue')
global string
global level
string ="0000000000""0000000000""0000000000""0000000000""0000000000""0000000000""0000000000""0000000000""0003000000""1111121111"
def makelevel():#creates level based on the string
    global string
    i = 0
    x = 0
    while i < 10:
        x = 0
        while x < 10:
            if string[i*10+x-0]=='0':
                canvas.create_rectangle(x*100,i*60,x*100+100,i*60+60,fill = 'white')
            elif string[i*10+x-0]=='2':
                canvas.create_rectangle(x*100,i*60,x*100+100,i*60+60,fill = 'red')
            elif string[i*10+x-0]=='3':
                canvas.create_rectangle(x*100,i*60,x*100+100,i*60+60,fill = 'yellow')
            else:
                canvas.create_rectangle(x*100,i*60,x*100+100,i*60+60,fill = 'black')
            x = x + 1
        i = i + 1
    recreate()
makelevel()
level = 0
def key(event):#detects when person presses key
    global yv
    global xv
    global jump
    jump = False
    key = event.keysym
    dire = 0
    if key == 'q':
        window.destroy()
    if key == "Up":
        jump = True
    else:
        jump = False
    if key == "Left":
        xv = -5
    if key == "Right":
        xv = 5
    if key == "s":
        nextlevel()
def release(event):#detects when person releases key
    global xv
    global jump
    if not jump:
        xv = 0
    else:
        jump = False
canvas.bind_all('<KeyPress>',key)
canvas.bind_all('<KeyRelease>',release)
global yv
global xv
global jump
jump = False
xv = 0
yv = 0
def nextlevel():#makes it next level
    global level
    global string
    level = level + 1
    if level == 1:
        string = "0000000000""0000000000""0000000000""0000000000""0000000000""0000000000""0000000000""0000100000""0000000000""1112221111"
    elif level == 2:
        string = "0000000000""0000000000""0200000000""0200000000""0222222222""0000000000""0000000000""0000000000""0000000000""1131313131"
    elif level == 3:
        string = "0000000000""0002000000""0002100100""0002000100""0001001100""0001000100""0001100100""0001000120""0000001100""1111111111"
    elif level == 4:
        string = "0000000000""0000000000""0000000000""0000000000""0000000000""0002000200""0002000200""0002000200""0001000100""1311113111"
    elif level   == 5:
        string = "0000000000""0000000000""0000000000""0000000000""0001010100""0002020200""0000000000""0001010100""0001010100""3333333333"
    elif level == 6:
        string = "0000000000""0001111110""0003300001""0001333002""0000001000""0000000333""0202020202""0000000002""0000000002""3333333333"
    elif level == 7:
        string = "0000000000""0000000000""0000010020""0033002330""0012010001""0030200310""0000010100""0001002000""0010010001""1111111111"
    elif level == 8:
        string = "0000000000""0000000000""0001212101""0100000001""0000000001""0212121001""0000000001""0000000011""0000000001""1212121212"
    else:
        window.destroy()
        print("YOU WIN!")
        pause = 0
        while True:
            pause = input("")
    makelevel()
def moverect():#moves the rectangle
    global yv
    global xv
    global jump
    yv = yv + 0.5
    if canvas.coords(a)[0] > 1000:#if it touches other side edge
        nextlevel()
    canvas.move(a,xv,0)#moves rectangle sideways
    canvas.move(a,0,yv)
    if string[int((((canvas.coords(a)[1]+20)//60))*10+((canvas.coords(a)[0]+40)//100))] == "1":#wall detection
        canvas.move(a,xv*-1,0)
    if string[int((((canvas.coords(a)[1]+20)//60))*10+((canvas.coords(a)[0])//100))] == "1":#wall detection
        canvas.move(a,xv*-1,0)
    if canvas.coords(a)[1] <=0 or string [int((((canvas.coords(a)[1])//60))*10+((canvas.coords(a)[0]+20)//100))] == "1":#ceiling detection
        canvas.move(a,0,yv*-1)
        yv = 0
        canvas.move(a,0,5)
    if string[int((((canvas.coords(a)[1]-20)//60+1))*10+((canvas.coords(a)[0]+20)//100))] == "1":#floor detection
        canvas.move(a,0,yv*-1)
        if yv > 0:
            yv = 0
        if jump == True:#jumping
            yv = -12
    if string[int((((canvas.coords(a)[1])//60))*10+((canvas.coords(a)[0]+20)//100))] == "2":#red detection
        recreate()
    if string[int((((canvas.coords(a)[1]+40)//60))*10+((canvas.coords(a)[0]+20)//100))] == "3":#yellow (bouncy) detection
        yv = -17
    window.after(16,moverect)#looping
moverect()
window.mainloop()#loops entire code