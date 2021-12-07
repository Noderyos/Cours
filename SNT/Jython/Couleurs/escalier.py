from gturtle import *

makeTurtle()
setPenColor("green")
setFillColor("green")
startPath()
right(45)
back(100)
forward(420)
left(135)
for i in range(3):
    forward(100)
    left(90)
    forward(100)
    right(90)
fillPath()
hideTurtle() 

