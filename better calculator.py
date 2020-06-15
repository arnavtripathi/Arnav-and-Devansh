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
