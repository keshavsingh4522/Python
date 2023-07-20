def print_numbers(n):
    if n == 0:
        return

    def print_recursive(t):
        if t == 0:
            return
        print_recursive(t - 1)
        print(t, end=' ')

    print_numbers(n - 1)
    print_recursive(n)
    print()

n = int(input('Enter a number: '))
print_numbers(n)

'''
output:
enter a number: 7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7
'''
