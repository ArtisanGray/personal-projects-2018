import random
def Ball():
  q = input("What would you like to ask the ball?\n")
  a = ["No", "Maybe", "Try Again", "Most Likely", "Yes"]
  print(a[random.randint(0,len(a)-1)])
  re = input("would you like to ask another question?: y/n --->")
  if re == "y":
    Ball()
Ball()
