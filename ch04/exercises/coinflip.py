import random
import turtle

window = turtle.Screen()
window.bgcolor('lightblue')
bird = turtle.Turtle()

pos = turtle.pos()
screen = window.screensize()



while pos <= screen:
  number = random.randrange(0,2)
  if number != 0:
    bird.left(90)
    bird.forward(50)
  elif number == 0:
    bird.right(90)
    bird.forward(50)
  pos = turtle.pos()

window.exitonclick()
  
