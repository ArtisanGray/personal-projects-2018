import random
def Roll_2():
  results = []
  rollNum = int(input("Enter number of dice to roll: "))
  numSides =  int(input("Enter number of sides the dice used have:"))
  for x in range(rollNum):
    results.append(random.randint(1, numSides))
  for y in range(len(results)):
    print("Roll #",y," produced a value of ",results[y])
    
Roll_2()
