from turtle import *
from random import *




def drawSquare(t,size):
    t.pd()
    t.pu()
    t.pd()
    t.begin_fill()
    t.fillcolor('blue')
    for _ in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()

def drawSquareFractal(t,size,step = 50):
    if size == 0:
        return
    t.fd(size / 1.5)
    t.lt(10)
    drawSquare(t,size)
    drawSquareFractal(t,size-1,step)

def     


t = Turtle()
t.speed(0)
colormode()

drawSquareFractal(t,50)
    



mainloop()