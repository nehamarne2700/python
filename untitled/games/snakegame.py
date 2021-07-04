import turtle
import random
from freegames import square,vector

food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)

def change(x,y):
    aim.x=x
    aim.y=y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head=snake[-1].copy()
    head.move(aim)

    if head in snake or not inside(head):
        square(head.x,head.y,9,'red')
        turtle.update()
        return

    snake.append(head)

    if head==food:
        print("Snake : ",len(snake))
        food.x=random.randrange(-15,15)*10
        food.y=random.randrange(-15,15)*10
    else:
        snake.pop(0)

    turtle.clear()

    for body in snake:
        square(body.x,body.y,9,'black')

    square(food.x,food.y,9,'green')
    turtle.update()
    turtle.ontimer(move,100)

#name=input("Enter Player Name : ")

turtle.setup(420,420,370,0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda :change(10,0),'Right')
turtle.onkey(lambda :change(-10,0),'Left')
turtle.onkey(lambda :change(0,10),'Up')
turtle.onkey(lambda :change(0,-10),'Down')
move()

turtle.done()

#print("**Snake Game Over ..."+name+"'s Final Snake Length : ",len(snake))