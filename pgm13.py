#nested if example to work in a company

age= int(input('Enter your age: '))

if age> 23:
    if age> 65:
        print('You cant work!!!')
    else:
        print('Welcome, you are of the right age!')
else:
    print('You are too young, go away!')
