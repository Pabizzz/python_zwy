# 开发者：Pabi
# 开发时间：2023/3/24 23:16
import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw the heart
t.penup()
t.goto(0, -150)
t.pendown()
t.begin_fill()
t.color('red')
t.pensize(10)
t.left(45)
t.forward(200)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)
t.forward(200)
t.end_fill()

# Write a message
t.penup()
t.goto(0, 50)
t.color('white')
t.write("I love you!", align="center", font=("Arial", 30, "bold"))

# Keep the window open until it is clicked
turtle.done()

