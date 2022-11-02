import turtle 
window = turtle.Screen()
dog = turtle.Turtle()

def triangle(x,y):
  dog.penup()
  dog.goto(x,y)
  dog.begin_fill()
  dog.color('black')
  dog.pendown()
  for i in range(3):
    dog.forward(30)
    dog.right(120)
  dog.end_fill()
  '''
  This function makes a black traingle
  args: (coords) The arguments are x,y coordinates where the shape 
  will start drawing
  return: nope
  '''

def uptriangle(x,y):
  dog.penup()
  dog.goto(x,y)
  dog.begin_fill()
  dog.color('black')
  dog.pendown()
  for i in range(3):
    dog.forward(30)
    dog.left(120)
  dog.end_fill()
  '''
  This function makes a black traingle upside down
  args: (coords) The arguments are x,y coordinates where the shape 
  will start drawing
  return: nope
  '''

def square(x,y):
  dog.penup()
  dog.goto(x,y)
  dog.begin_fill()
  dog.color('brown')
  dog.pendown()
  for i in range (3):
    dog.forward(35)
    dog.left(90)
  dog.end_fill()
  '''
  This function makes a brown square
  args: (coords) The arguments are x,y coordinates where the shape 
  will start drawing
  return: nope
  '''

def halmessage(age):
  if age >= 15:
    message = "Have fun handing out candy!"
    return message
  elif age < 15:
    message = "Have fun trick or treating!"
    return message
  '''
  This function asks for age and returns a message
  args: (int) The argument is the age of the user
  return: (string) One of the two messages 
  ''' 

def main():
  
  dog.hideturtle()
  dog.penup()        #circle
  dog.goto(0,-85)
  dog.color('dark orange')
  dog.begin_fill()
  dog.circle(100)
  dog.end_fill()

  triangle(-50,-15)  #teeth
  triangle(-20,-15)
  triangle(10,-15)
  
  uptriangle(-45,35) #eyes
  uptriangle(5,35)

  square(-10,90)

  age = int(input("How old are you:"))
  dog.penup()
  dog.goto(0,-105)
  dog.pendown()
  dog.write(halmessage(age),move=False,align='center',font= 
  ('arial','12','normal'))

  window.exitonclick()
main()