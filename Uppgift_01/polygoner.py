import turtle as t
tim = t.Turtle() # Sköldpaddan kan döpas till vilket variabelnamn som helst
# tim.hideturtle() # Kan avkommenteras när programmet är klart
tim.pensize(5.0) # Kan vara vilket tal x som helst, x > 0
tim.shape("turtle")
tim.shapesize(2.0) # Kan vara vilket tal x som helst, x > 0
tim.speed(2) # Heltal 0 - 10 (1 - 10 ökande hastighet, 0 är snabbast)
screen = t.Screen()
screen.bgcolor("wheat1")

def move_to(x, y, mark=False):
    if not mark:
        tim.penup() # Normalt så ritas ett streck efter sköldpaddans väg, penup() ändrar på det
    tim.goto(x, y)
    tim.pendown() # Glöm inte att sätta ned pennan igen där det behövs

move_to(-100, 50)

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