ADULT_TIX = 15.00
CHILD_TIX = 8.00
SENIOR_TIX = 10.00

age = int(input('Please enter your age so we can calculate ticket price: '))

if age < 18:
    print('Price is', '%.2f' % CHILD_TIX)
elif age > 64:
    print('Price is', '%.2f' % SENIOR_TIX)
else:
    print('Price is', '%.2f' % ADULT_TIX)
