from tkinter import *

class Rectangle:

    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


def draw_rectangle(canvas,rect):

    x1 = rect.x
    y1 = rect.y
    x2 = rect.x + rect.width
    y2 = rect.y + rect.height

    canvas.create_rectangle(x1,y1,x2,y2,fill=rect.color)


root = Tk()

canvas = Canvas(root,width=400,height=400)
canvas.pack()

r = Rectangle(50,60,150,100,"blue")

draw_rectangle(canvas,r)

root.mainloop()
