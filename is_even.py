num=int(input("Enter number to check even or odd\n"))
def Is_Even(num):
    return f"{num} is even " if num%2==0 else f"{num} is odd"
print(Is_Even(num))
