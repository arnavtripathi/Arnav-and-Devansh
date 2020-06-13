import turtle

wn = turtle.Screen()
wn.title("Letter to Arnav Tripathi")
wn.bgcolor("forestgreen")
wn.setup(width=900, height=600)
wn.tracer(0)

iv = turtle.Turtle()
iv.color("white")
iv.penup()
iv.hideturtle()
iv.goto(0,160)
iv.write("But at least i have a life unlike u! ", align="center", font=("Courier", 30, "normal"))

ik = turtle.Turtle()
ik.color("white")
ik.penup()
ik.hideturtle()
ik.goto(0, 100)
ik.write("Just like a ming chong and ding dong! ", align="center", font=("Courier", 30, "normal"))
