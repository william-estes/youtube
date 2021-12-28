def add_numbers(x, y):
    return x + y

print(add_numbers(1, 2))

##############################

def describe_pet(pet_name, animal_type):
    print(f'{pet_name.title()} is a {animal_type}')

describe_pet(animal_type='dog', pet_name='Spot')

###############################

def describe_pet_default(pet_name, animal_type='dog'):
    print(f'{pet_name.title()} is a {animal_type}')

describe_pet_default(pet_name='Spot')

###############################

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

name = get_formatted_name('Jimi', 'Hendrix')
print(name)
name = get_formatted_name('John', 'Wick', 'Michael')
print(name)

#################################


