from turtle import *
import obj
def square(x):
    fd(x)
    left(90)
    fd(x)
    left(90)
    fd(x)
    left(90)
    fd(x)

def triangle(x):
    fd(x)
    left(120)
    fd(x)
    left(120)
    fd(x)

def rectangle(x,y):
    fd(x)
    left(90)
    fd(y)
    left(90)
    fd(x)
    left(90)
    fd(y)

def cube():
    obj.print()

def circle(x):
    t = Turtle()
    t.circle(x)
    
def pattern(x,y):
    for i in range(int(360/x)):
        square(y)
        left(x)
    
    
