isDiv = 0
mul = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(2520, 9999999999, 2520):
  for x in mul:  
    if i%x == 0:isDiv += 1
  if isDiv == len(mul): print("True", i);break
  isDiv = 0
