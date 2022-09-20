import random


number = random.randrange(0,11)


for i in range(3):
  guess=int(input("What is your guess:"))
  if guess < number:
    print("Too low")
  if guess > number:
    print("Too high")
  if guess == number:
    print("correct!")
    break
