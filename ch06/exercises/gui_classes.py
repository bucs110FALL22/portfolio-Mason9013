class Mario: 
  def __init__(self):
    self.jump = False #only true when user hits jump
    self.crouch = False 
    self.coins = 22

class Goomba:
  def __init__(self):
    self.move = True #move infinitely
    self.num = 1
    self.alive = True

class Brick:
  def __init__(self):
    self.present = True #false when hit
    self.coins = 1
    self.height = 4
