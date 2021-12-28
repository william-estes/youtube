my_dict = {}  # can be declared as my_dict = dict() 

# add key/value pairs
my_dict['first_name'] = 'Will'  # create a key/value pair of first_name:Will
my_dict['last_name'] = 'Estes'
my_dict['salary'] = 50_000
my_dict['position'] = 'Software Engineer'  

# overwrite key/value pairs
my_dict['first_name'] = 'Tom'  # overwrite existing key/value pair of first_name:Will
my_dict['last_name'] = 'Ford'  

# accessing elements
print(my_dict['first_name'])
print(my_dict.get('last_name'))
print(my_dict.get('middle_name', 'N/A'))  # outputs N/A since middle_name isn't in our dictionary
print(my_dict.get('occupation'))  # outputs None since this key/value pair doesn't exist and no default provided

# remove elements
print(my_dict.pop('salary'))
print(my_dict.popitem())
my_dict.clear()
print(my_dict)
