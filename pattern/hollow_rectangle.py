n=10
for row in range(n):
    if (row==0 or row==n-1):
        for i in range(n):
            print("*",end=" ")
        print("\n")
    else:
        for i in range(n):
            if(i==0 or i==n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")
