import pygame
pygame.init()
display = pygame.display.set_mode()

n = 101
countuno = 0
while n != 1:
  if n % 2 == 0:
    n = n/2
  elif n % 2 != 0:
    n = 3*n+1
  #print(n)
  countuno += 1
print(countuno)


first_upper_limit = 20
first_start = range(2,first_upper_limit+1)
first_iters= {}

for i in first_start:
  countt = 0
  n = i
  while n !=1:
    countt += 1
    if n%2==0:
      n=n/2
    else:
      n = 3*n+1
  first_iters[i] = countt
print(first_iters)

pygame.display.flip()

itersDict = {}
maxSoFar = 0
maxVal = 0

font = pygame.font.Font(None,18)

for x in range(2, first_upper_limit):
  count = 0
  n = x
  while n !=1:
    if n%2==0:
      n=n/2
    else:
      n = (3*n)+1
    count += 1
  itersDict[x*15] = (count*15)
pygame.display.flip()          

if len(itersDict) >= 2:
  pygame.draw.lines(display, "orange", False, list(itersDict.items()))
pygame.display.flip()          

flipDisplay = pygame.transform.flip(display, False, True)
pygame.display.flip()
display.blit(flipDisplay, (0,0))
pygame.display.flip()

if maxSoFar < count:
  maxSoFar = count
  maxVal = x
pygame.display.flip()
message = font.render(str(maxSoFar),False, "Blue")
display.blit(message, (10,10))

pygame.display.flip()


