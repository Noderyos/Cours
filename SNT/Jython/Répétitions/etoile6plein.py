from gturtle import *

makeTurtle()
hideTurtle()
setPenColor("red")
setFillColor("red")
startPath()
for i in range(6):
    forward(50)
    right(140)
    forward(50)
    left(80)
fillPath()
