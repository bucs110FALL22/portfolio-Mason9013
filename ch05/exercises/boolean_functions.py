def percentage_to_letter(score=0):
  if score >= 90:
    letter = "A"
    return letter
  elif score >= 80:
    letter = "B"
    return letter
  elif score >= 70:
    letter = "C"
    return letter
  elif score >= 60:
    letter = "D"
    return letter
  elif score < 60:
    letter = "F"
    return letter

def is_passing(letter):
  if letter == "A":
    x = True
  elif letter == "B":
    x = True
  elif letter == "C":
    x = True
  else:
    x = False
  return x

your_score = int(input("Please input your score:"))

grade = percentage_to_letter(score=your_score)

print(grade)

print(is_passing(grade))
  