from gturtle import *

makeTurtle()
hideTurtle()
def square():
    for i in range(4):
        forward(50)
        right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
right(45)
setPenColor("red")
square()
setPenColor("green")
square()
setPenColor("blue")
square()
setPenColor("black")
square()
