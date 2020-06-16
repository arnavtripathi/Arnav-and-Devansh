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
Leg1.color("blue")
Leg1.shapesize(stretch_wid=5, stretch_len=0.5)
Leg1.penup()
Leg1.goto(-33,-140)
Leg1.right(45) 

Leg2 = turtle.Turtle()
Leg2.speed(0)
Leg2.shape("square")
Leg2.color("blue")
Leg2.shapesize(stretch_wid=5, stretch_len=0.5)
Leg2.penup()
Leg2.left(45)
Leg2.goto(33,-140)
Leg2.goto(33,-140)

Arm1 = turtle.Turtle()
Arm1.speed(0)
Arm1.shape("square")
Arm1.color("purple")
Arm1.shapesize(stretch_wid=7, stretch_len=0.5)
Arm1.penup()
Arm1.left(45)
Arm1.goto(-50,150)

Arm2 = turtle.Turtle()
Arm2.speed(0)
Arm2.shape("square")
Arm2.color("purple")
Arm2.shapesize(stretch_wid=7, stretch_len=0.5)
Arm2.penup()
Arm2.right(45)
Arm2.goto(50,150)

