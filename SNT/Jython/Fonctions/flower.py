from gturtle import *

makeTurtle()
hideTurtle()
def arc():
    for i in range(90):
        forward(2)
        right(1)
def flower():
    startPath()
    for i in range(5):
        arc()
        right(90)
        arc()
        right(18)
    fillPath()
setPenColor("red")
setFillColor("red")
flower()
