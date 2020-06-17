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

Mouth1 = turtle.Turtle()
Mouth1.speed(0)
Mouth1.shape("circle")
Mouth1.color("red")
Mouth1.shapesize(stretch_wid=0.5, stretch_len=2)
Mouth1.penup()
Mouth1.goto(2,175)

Eye1 = turtle.Turtle()
Eye1.speed(0)
Eye1.shape("circle")
Eye1.color("orange")
Eye1.shapesize(stretch_wid=.5, stretch_len=.5)
Eye1.penup()
Eye1.goto(-20,200)

Eye2 = turtle.Turtle()
Eye2.speed(0)
Eye2.shape("circle")
Eye2.color("orange")
Eye2.shapesize(stretch_wid=.5, stretch_len=.5)
Eye2.penup()
Eye2.goto(20,200)

Hat1 = turtle.Turtle()
Hat1.speed(0)
Hat1.shape("square")
Hat1.color("black")
Hat1.shapesize(stretch_wid =.6, stretch_len=6.5)
Hat1.penup()
Hat1.goto(0, 250)

Hat2 = turtle.Turtle()
Hat2.speed(0)
Hat2.shape("square")
Hat2.color("black")
Hat2.shapesize(stretch_wid =2, stretch_len=4)
Hat2.penup()
Hat2.goto(0, 270)
while True:
    Arm1.speed(2)
    while Arm1.left(45):
        Arm1.right(45)
    while Arm1.right(45):
        Arm1.left(45)
    Arm2.speed(2)
    while Arm2.right(45):
        Arm2.left(45)
    while Arm2.left(45):
        Arm2.right(45)

