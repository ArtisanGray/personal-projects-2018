init_ = int(input("Enter the starting number to look for palindromes in: "))
end = int(input("Enter the end number to look for palindromes in: "))
def findLP(a,b):
  palindromes = []; x = a; y = a; countLoop = 0
  for z in range(a,b):
    for i in range(a,b):
      xstr = str(x*y); y+=1;
      if xstr[0::] == xstr[::-1]: palindromes.append(int(xstr))
    y = a; x += 1; countLoop += 1
  pOrder = sorted(palindromes)
  print("\n The largest palindrome made from two products in the range of ",a," through ",b," is ",pOrder[len(pOrder)-1])
findLP(init_, end)
