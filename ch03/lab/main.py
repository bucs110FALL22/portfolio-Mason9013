import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange (1,101)
y= random.randrange (1,101)
michelangelo.forward(x)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(1,21):
  if i % 2 == 0:
    michelangelo.forward (random.randrange(1,11))
  if i % 2 != 0:
    leonardo.forward(random.randrange(1,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  
# PART B - complete part B here


for num_sides in 

pygame.init()
window = pygame.display.set_mode()

window.exitonclick()
