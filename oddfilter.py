odd = [2, 3, 4, 5, 6, 77, 65, 44, 99]
new = list(filter(lambda x: x % 2 != 0, odd))
print(new)
