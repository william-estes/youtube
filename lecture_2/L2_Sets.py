my_set = set()

my_set.add('apple')
my_set.add('banana')
my_set.add('cherry')

print('banana' in my_set)    # outputs True since 'banana' is in my_set

my_set.update(['lime', 'lemon']) # add multiple items to my_set

print(my_set)

my_set.discard('cherry') # remove 'cherry' if it exists

print(my_set)