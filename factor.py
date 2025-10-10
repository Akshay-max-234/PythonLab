fact=int(input("Enter a number:"))
print("Factors of",fact, "are:")
for i in range(1,fact+1):
  if fact %i==0:
   print(i)

 