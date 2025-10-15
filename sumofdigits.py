def sumofdigits(n):
    sum = 0
    while n > 0:
        digits = n % 10
        sum += digits
        n = n // 10
    return sum
n = int(input("Enter the number: "))
print("Sum of digits:", sumofdigits(n))

       
        
        