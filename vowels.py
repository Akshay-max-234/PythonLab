v=['a','e','i','o','u','A','E','I','O','U']
a=input("Enter the String:")
count=0
for i in range (len(a)):
    if a[i] in v:
        count+=1
        print("The Number of Vowels:",count)