def mult(num1,num2):
 product = 0
 for i in range(num1):
  product = product + num2
 return product
"""
This function multiplies
args: num1,num2
return: int
"""

def expon(num3,exponent):
  power = 1
  for i in range(exponent):
    power = power * num3
  return power
"""
This function does exponents
args: num3,exponent
return: int
"""

def square(num4):
  return mult(num4,num4)
"""
This function squares
args: num4
return: int
"""

def main():
  number1 = int(input("Number to be muliplied:"))
  number2 = int(input("Number to multiply:"))
  print(mult(number1,number2))

  number3 = int(input("Number to be exponented:"))
  exponented = int(input("Exponent:"))
  print(expon(number3,exponented))
  
  number4 = int(input("Number to be squared:"))
  print(square(number4))
  
main()
