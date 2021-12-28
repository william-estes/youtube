names = ['Will', 'Amy', 'Tim', 'Bob', 'Susan', 'Sara'] 

# accessing list elements
print(names[0])           # outputs 'Will' since that's the element at index 0

# modifying lists
names[0] = 'Richard'      # changes 'Will' to 'Richard'

names.append('Molly')     # adds 'Molly' to the end of the list
names.insert(1, 'Ted')    # adds 'Ted' at position 1, shifts the rest of the elements right by 1

del names[1]              # removes the element at index 1
person = names.pop()      # removes last element and returns it so it's available to use in a print() or variable
person2 = names.pop(2)    # removes specified element at index and returns it so it's available to use in a print() or variable
names.remove('Bob')       # removes first occurence of element in list

print(names)
print(len(names))