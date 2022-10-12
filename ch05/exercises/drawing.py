import turtle
import math

def drawEqShape(myturtle, num_sides, side_length):
  for s in range(num_sides):
   theta = 360 / num_sides
   myturtle.forward(side_length)
   myturtle.right(theta)
   window.delay(100)

window = turtle.Screen()
John = turtle.Turtle()
John.shape('turtle')
John.color('green')

num_sides = int(input("How many sides would you like:"))

side_length = int(input("How long should each side be:"))

drawEqShape(John, num_sides, side_length)

window.exitonclick()
