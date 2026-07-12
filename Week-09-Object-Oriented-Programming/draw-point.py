from tkinter import *

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y


def draw_point(canvas,p):

    x = p.x
    y = p.y

    canvas.create_oval(x-2,y-2,x+2,y+2,fill="black")


root = Tk()

canvas = Canvas(root,width=400,height=400)
canvas.pack()

p = Point(200,200)

draw_point(canvas,p)

root.mainloop()
