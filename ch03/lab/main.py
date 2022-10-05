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
pygame.init()
window = pygame.display.set_mode()

green = (0,255,0)
blue = (0,0,255)
window.fill(green)

coords = []
num_sides = 3
side_length = int(80)
offset = int(150)
for s in range(3):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)

coords = []
num_sides = 4
side_length = int(80)
offset = int(150)
for s in range(4):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)

coords = []
num_sides = 6
side_length = int(80)
offset = int(150)
for s in range(6):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)

coords = []
num_sides = 6
side_length = int(80)
offset = int(150)
for s in range(6):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)

coords = []
num_sides = 9
side_length = int(80)
offset = int(150)
for s in range(9):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)

coords = []
num_sides = 360
side_length = int(80)
offset = int(150)
for s in range(360):
  theta = (2.0 * math.pi * (s)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append ((x,y))
pygame.draw.polygon(window,blue,coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)