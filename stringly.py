l = input("Enter a string: ")
length = len(l)
if length > 2:
    if l[-3:] == "ing":
        l += "ly"
    else:
        l += "ing"
    print(l)
 
