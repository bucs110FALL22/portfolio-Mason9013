class Rectangle:
  def __init__(self,x,y,h,w):
    
    if x < 0:
      x = 0
    if y < 0:
      y = 0
    if h < 0:
      h = 0
    if w < 0:
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  '''
  This function takes x,y coordinates as well as heighth and width numbers. It also sets these to zero if they are negative.
  args: (obj) self, (int) xcoord, (int) ycoord, (int) height, (int) width
  return: none
  '''

  def __str__(self):
    return f"x: {self.x}, y: {self.y}, Height: {self.height}, Width: {self.width}"

  '''
  This function makes a string describing rectangle stats
  args: (obj): self
  return: The string
  '''

    
        