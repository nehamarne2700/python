import turtle

wn=turtle.Screen()
wn.bgcolor("black")
colors=["red","purple","blue","green","orange","yellow","white"]
draw=turtle.Turtle()
for x in range(360):
    draw.pencolor(colors[x%7])
    draw.width(x/120+1)
    draw.forward(x)
    draw.left(51)
turtle.done()