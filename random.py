#-------------------------------------------------------------------------------
# Name:        Turtle
# Purpose:
#
# Author:      Alfian
#
# Created:      27/03/2019
# Copyright:    Everyone
# Licence:      MIT License 
#-------------------------------------------------------------------------------

import turtle
wn =turtle.Screen()
wn.bgcolor("black")
wn.title("Color Array")
mynewarrow = turtle.Turtle()
mynewarrow.color("white")
mynewarrow.pensize(3)
for i in range(3):
    mynewarrow.forward(50)
    mynewarrow.left(120)
    mynewarrow.forward(50)
turtle.mainloop()
