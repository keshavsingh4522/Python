num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
choice = input('Enter operator: ')
 
if choice == '+':
    print(num_1 + num_2)
 
elif choice == '-':
    print(num_1 - num_2)
 
elif choice == '*':
    print(num_1 * num_2)
 
elif choice == '/':
    print(num_1 / num_2)
 
else:
    print('Enter a valid operator, please run the program again.')
