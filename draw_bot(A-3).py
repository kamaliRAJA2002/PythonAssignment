from shapes import *
print(" 'q' to stop")
while True:
    p= input("enter the shape you want to draw : ")
    p = p.lower()
    if p == 'circle':
        circle(int(input(" enter the radius of the circle : ")))
    elif p == 'rectangle' :
        rectangle(100,50)
    elif p == 'square' :
        square(50)
    elif p == 'cube':
        cube()
    elif p== 'triangle':
        triangle(100)
    elif p == 'pattern' :
        pattern(10,50)
    elif p == 'q':
        break
