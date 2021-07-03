import turtle as t
tim = t.Turtle()
tim.hideturtle()
tim.pensize(5)
tim.shape("triangle")
tim.shapesize(0.5)
tim.speed(0) # 0 - 10
screen = t.Screen()

def goto(x, y, mark=False):
    if not mark:
        tim.penup()
    tim.goto(x, y)
    tim.pendown()

goto(-200, -100)

# Nedanstående förflyttningar görs
# med fördel i en loop.
tim.color('DarkBlue','azure2')
tim.begin_fill()
tim.forward(150)
tim.right(90)
tim.forward(150)
tim.right(90)
tim.forward(150)
tim.right(90)
tim.forward(150)
tim.right(90)
tim.end_fill()


screen.exitonclick()