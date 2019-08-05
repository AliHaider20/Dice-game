import random
print("Dice Roll Game")
print("Press enter  for ending game")
while True:
  try:
    start=int(input("Enter the start value"))
    end=int(input("Enter the end value"))
  except ValueError:
    break
  if start>=1 and end<=6:
    num=random.randint(start,end)
    print(num)
  else:
    print("invalid number")


