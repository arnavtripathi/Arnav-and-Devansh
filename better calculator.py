import turtle

wn = turtle.Screen()
wn.title("Stickman 1.1")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)


head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.shapesize(stretch_wid=5, stretch_len=5)
head.penup()
head.goto(0,200)

neck = turtle.Turtle()
neck.speed(0)
neck.shape("square")
neck.color("forestgreen")
neck.shapesize(stretch_wid=13, stretch_len=0.5)
neck.penup()
neck.goto(0,18.5)

Leg1 = turtle.Turtle()
Leg1.speed(0)
Leg1.shape("square")
Leg1.color("forestgreen")
Leg1.shapesize(stretch_wid=13, stretch_len=0.5)
Leg1.penup()
Leg1.goto(0,18.5)

neck = turtle.Turtle()
neck.speed(0)
neck.shape("square")
neck.color("forestgreen")
neck.shapesize(stretch_wid=13, stretch_len=0.5)
neck.penup()
neck.goto(0,18.5)