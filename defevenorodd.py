def evenodd(b):
    if b % 2 == 0:
        return "Even"
    else:
        return "Odd"
b = int(input("Enter a number: "))
print("The number is", evenodd(b))
