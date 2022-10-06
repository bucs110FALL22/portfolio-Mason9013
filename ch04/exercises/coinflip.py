import random
import turtle

window = turtle.Screen()
window.bgcolor('lightblue')
bird = turtle.Turtle()

pos = turtle.pos()
screen = window.screensize()

print(window.screensize()) #(400,300)
print(turtle.pos())

while bird.xcor() <= 200 and bird.xcor() >= -200 and bird.ycor() <= 150 and bird.ycor() >= -150:
  number = random.randrange(0,2)
  if number != 0:
    bird.left(90)
    bird.forward(50)
    bird.xcor()
    bird.ycor()
  elif number == 0:
    bird.right(90)
    bird.forward(50)
    bird.xcor()
    bird.ycor()
    
    

window.exitonclick()
  
  
