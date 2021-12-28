def add_one(num):
    num += 1
    
my_num = 0
add_one(my_num)
print(my_num)       # outputs 0

def change_dict(d):
    d['abcd'] = 1234

my_dict = {}
change_dict(my_dict)
print(my_dict)      # outputs {'abcd':1234}

def change_list(l):
    l.append('a')

li = []
change_list(li)
print(li)           # outputs ['a']