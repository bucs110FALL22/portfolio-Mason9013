import turtle

sides = int(input("How many sides do you want:"))
length = int(input("How long do you want each side to be:"))

cat = turtle.Turtle()
cat.color("red")

angle = 360/sides

for i in [angle]*sides:
  cat.forward(length)
  cat.left(i)

window = turtle.Screen()
window.exitonclick()
