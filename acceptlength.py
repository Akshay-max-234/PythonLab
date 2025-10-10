j = input("Enter the words: ").split()
longest = 0
for word in j:
    if len(word) > longest:
        longest = len(j)
print("Length of the longest word:", longest)
