import tkinter as tk
from random import choice
# =========================================
col1 = 'white' # background
col2 = 'black' # points, text

x = 960
y = 540
size = 10
# =========================================
def create(x,y,size):
    c.create_rectangle(x, y,
                       x+size, y + size,
                       fill=col2, outline=col2)

def delete(x,y,size):
    c.create_rectangle(x, y,
                       x + size, y + size,
                       fill=col1, outline=col2)

def moveleft():
    global x
    delete(x,y,size)
    x-=size
    x=x % (1920 - 1920%size)  #+ size
    create(x,y,size)

def moveright():
    global x
    delete(x, y, size)
    x += size
    x = x % (1920 - 1920%size) #- size
    create(x, y, size)

def moveup():
    global y
    delete(x, y, size)
    y -= size
    y = y % (1080 - 1080%size) #- size
    create(x, y, size)

def movedown():
    global y
    delete(x, y, size)
    y += size
    y = y % (1080 - 1080%size) #+ size
    create(x, y, size)

def move(m: str):
    if m == 'u':
        moveup()
    elif m == 'd':
        movedown()
    elif m == 'l':
        moveleft()
    elif m == 'r':
        moveright()
    return

def start(event):
    global pace
    c.create_rectangle(0,0,1920,1080,fill=col1)
    window.bind('<space>', func = nothing)
    while True:
        # pace += 1
        # c.create_rectangle(0,0,100,100,fill=col1)
        # c.create_text(50,50,text=str(pace), font='Arial 14', fill=col2)
        move(choice(moves))
        window.update()

def changetheme(event):
    global col1
    global col2
    g = col1
    col1 = col2
    col2 = g
    c.create_rectangle(0, 0, 1920, 1080, fill=col1)
    c.create_text(960, 100, text='Press Enter to start', font='Arial 100', fill=col2)
    c.create_text(960, 200, text='Press space to change color scheme', font='Arial 30', fill=col2)
    create(x, y, size)
    window.update()

def increase(event):
    global size
    global x
    global y
    c.create_rectangle(x, y,
                       x + size, y + size,
                       fill=col1, outline=col1)
    size+=1
    if size==0:
        size+=1
    create(x,y,size)
    window.update()

def decrease(event):
    global size
    c.create_rectangle(x, y,
                       x + size, y + size,
                       fill=col1, outline=col1)
    size-=1
    if size==0:
        size-=1
    create(x,y,size)
def nothing(event):
    pass

window = tk.Tk()
window.geometry("1920x1080+0+0")

c = tk.Canvas(window, bg=col1, height=1080, width=1920)
c.pack()

moves = ['u','d','l','r']

pace = 0



create(x,y,size)
c.create_text(960,100,text='Press Enter to start', font='Arial 100', fill=col2)
c.create_text(960,200, text='Press space to change color scheme', font='Arial 30',  fill=col2)

window.bind('<Return>',func=start)
window.bind('<space>', func=changetheme)
window.bind('<=>', func=increase)
window.bind('<minus>', func=decrease)


window.mainloop()

