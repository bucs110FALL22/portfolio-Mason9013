import time

class Animal:
  def __init__ (self, name, type):
    self.id = time.strftime("%d%m%M%S")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None

  def setAdopted():
    self.adopted = time.strftime("%d/%m/%Y")

def main():
  smudge = Animal("smudge","dog")
  smudge.setAdopted()
  print(smudge)
main()
    