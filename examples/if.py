# If statement example

number = input('Enter a number: ')

if number >= 1 and number <= 4:
    print('Between 1 e 4')
elif number >= 5 and number <= 8:
    print('Between 5 e 8')
elif number >= 9 and number <= 10:
    print('Between 9 e 10')
else:
    print('Out of range')