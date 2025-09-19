list1 = [123, 'abcd', 3.4, 'TOM', 34.6]
list2 = ['abc', 9, 'efg', 1.4]

print(list1 + list2)         
print(len(list1))            
list1.append(100)            
print(list1)
print(list1.count('efg'))    
list1.remove('TOM')          
print(list1)
list1.insert(2, '3310')      
print(list1)