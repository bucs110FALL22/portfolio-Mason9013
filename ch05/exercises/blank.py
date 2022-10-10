def star_pyramid(): 
  rows = int(input("How many rows would you like:"))

  for i in range(rows+1):
    print(i*"*")
    
star_pyramid()

def rstar_pyramid():
  rows = int(input("How many rows would you like:"))
  
  while rows > 0:
    print(rows*"*")
    rows -= 1 

rstar_pyramid()
    