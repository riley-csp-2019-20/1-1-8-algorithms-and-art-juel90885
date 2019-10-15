# creating the turtle 
import turtle as trtl
import random
pig = trtl.Turtle()
pig.hideturtle()
pig.speed(0)

# create head
pig.fillcolor("#b4dadb")
pig.begin_fill()
pig.penup()
pig.goto(0,75)
pig.pendown()
pig.circle(60)
pig.penup()
pig.end_fill()

# create eye
pig.fillcolor("white")
pig.begin_fill()
pig.goto(0,100)
pig.pendown()
pig.circle(40)
pig.end_fill()



# create the beak
pig.fillcolor("#dece6e")
pig.setheading(4)
pig.begin_fill()
pig.penup()
pig.goto(-60,135)
pig.pendown()
pig.circle(30,360,3)
pig.end_fill()

# create the legs and feet
pig.pensize(20)
pig.pencolor("#b4dadb")
pig.setheading(270)
pig.penup()
pig.goto(-16,76)
pig.pendown()
pig.forward(100)
pig.setheading(180)
pig.forward(20)

pig.setheading(270)
pig.penup()
pig.goto(16,76)
pig.pendown()
pig.forward(100)
pig.setheading(180)
pig.forward(-20)

while True:
    # this is for pupil 
    pig.pensize(1)
    pig.fillcolor(random.choice(["red", "yellow", "green", "blue"]))
    pig.begin_fill()
    pig.penup()
    pig.goto(10,167)
    pig.pendown()
    pig.circle(25)
    pig.end_fill()


wn= trtl.Screen()
wn.mainloop()