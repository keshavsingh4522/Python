def Fibonacci_Self(number):
    PN = 0
    CN = 1
    if number == 0:
        return 0
    for i in range(1, number):
        PPN = PN
        PN = CN
        CN = PPN + PN
    return CN

if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number: "))
        except Exception as E:
            print("Only integers are allowed...!")
            continue
        else:
            print(f'The fibonacci series for {number} number is {Fibonacci_Self(number=number)}')
        continue
