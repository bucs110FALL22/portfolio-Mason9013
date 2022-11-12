import pygame 
import random
import math

pygame.init()

window = pygame.display.set_mode((320,320))
window.fill("blue")
surface = pygame.display.get_surface()

screenxy = pygame.display.get_window_size()
width = screenxy[0]
height = screenxy[1]

pygame.draw.circle(surface, "red", (160,160), 160)
pygame.draw.line(surface, "black",(0,160),(320,160))
pygame.draw.line(surface, "black",(160,0),(160,320))
pygame.display.flip()

for i in range(10):
  xcoord = random.randrange(0,width)
  ycoord = random.randrange(0,height)

  distance_from_center = math.hypot(xcoord-(width/2),ycoord-(height/2))
  is_in_circle = distance_from_center <= width/2

  if is_in_circle:
    pygame.draw.circle(surface, "green",(xcoord,ycoord),5)
  else:
    pygame.draw.circle(surface, "orange",(xcoord,ycoord),5)

  pygame.display.flip()
  pygame.time.wait(800)

#User chooses a player
window.fill("black")

pygame.draw.polygon(surface, "red", [(100,50),(220,50),(220,100),(100,100)])
pygame.draw.polygon(surface, "blue", [(100,150),(220,150),(220,200),(100,200)])
pygame.display.flip()
print("Click on the player you think will win")

choice = ""
clicked = False
while clicked == False:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      clickcoords = pygame.mouse.get_pos()
      if clickcoords[0]>100 and clickcoords[0]<220 and clickcoords[1]>50 and clickcoords[1]<100:
        choice = "red"
        clicked = True
        print("you chose red")
      if clickcoords[0]>100 and clickcoords[0]<220 and clickcoords[1]<200 and clickcoords[1]>150:
        choice = "blue"
        clicked = True
        print("you chose blue")
pygame.display.flip()


#redraw board
window.fill("white")
pygame.draw.circle(surface, "green", (160,160), 160)
pygame.draw.line(surface, "black",(0,160),(320,160))
pygame.draw.line(surface, "black",(160,0),(160,320))
pygame.display.flip()


#Two players play
redPoints = 0
bluePoints = 0
for i in range(10):
  xcoord = random.randrange(0,width)
  ycoord = random.randrange(0,height)

  distance_from_center = math.hypot(xcoord-(width/2),ycoord-(height/2))
  is_in_circle = distance_from_center <= width/2
  
  if i%2==0:
    #red
    if is_in_circle:
     pygame.draw.circle(surface, "red",(xcoord,ycoord),5)
     redPoints += 1
    else:
     pygame.draw.circle(surface, "orange",(xcoord,ycoord),5)
  if i%2!=0:
    #blue
    if is_in_circle:
     pygame.draw.circle(surface, "blue",(xcoord,ycoord),5)
     bluePoints += 1
    else:
     pygame.draw.circle(surface, "brown",(xcoord,ycoord),5)
  pygame.display.flip()
  pygame.time.wait(800)

winner =""

if redPoints > bluePoints:
    print("Red won")
    winner = "red"
elif bluePoints > redPoints:
    winner = "blue"
    print("Blue won")
elif bluePoints == redPoints:
  print("Red and blue drew")
  winner == "Neither"

if winner == choice:
    print("Congradulations you guessed the winner")
elif winner != choice:
    print("You did not predict the winner")
    if redPoints == bluePoints:
     print("but that is because it was a draw")

