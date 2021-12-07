from gturtle import *

makeTurtle()
hideTurtle()
def arc():
    for i in range(90):
        forward(2)
        right(1)
setPenColor("red")
setFillColor("red")
startPath()
arc()
right(90)
arc()
fillPath()
