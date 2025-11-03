def factorial(n): 
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter the number: "))
if num >= 1:
    print("Factorial:", factorial(num))
