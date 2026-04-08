# Josue VillaBonilla
# 7 APR 2026
# P4LAB1
# This program draws a square and triangle using loops.

import turtle

wn = turtle.Screen()
wn.bgcolor("skyblue")
wn.title("House Drawing")

tess = turtle.Turtle()
tess.color("green")
tess.pensize(5)

# Draw square using FOR loop
for x in range(4):
    tess.forward(100)
    tess.left(90)

# Move to top-left corner of square
tess.left(90)
tess.forward(100)
tess.right(90)

# Fill triangle
tess.fillcolor("red")
tess.begin_fill()

# Draw triangle using WHILE loop
count = 0
while count < 3:
    tess.forward(100)
    tess.left(120)
    count = count + 1

tess.end_fill()

wn.mainloop()