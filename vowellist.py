a=input("Enter a string:")
vowel=('a','e','i','o','u','A','E','I','O','U')
vowellist = []

for c in a:
    if c in vowel:
        vowellist.append(c)

print(vowellist)