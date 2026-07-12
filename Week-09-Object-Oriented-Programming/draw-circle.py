from tkinter import *

class Circle:

    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


def draw_circle(canvas,c):

    x1 = c.x - c.radius
    y1 = c.y - c.radius
    x2 = c.x + c.radius
    y2 = c.y + c.radius

    canvas.create_oval(x1,y1,x2,y2,fill=c.color)


root = Tk()

canvas = Canvas(root,width=400,height=400)
canvas.pack()

c1 = Circle(200,200,80,"red")
c2 = Circle(100,100,40,"green")

draw_circle(canvas,c1)
draw_circle(canvas,c2)

root.mainloop()
