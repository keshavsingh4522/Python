s=6
k=3*s-3
for i in range(0,s):
    for j in range(0,k):
        print(end=" ")
    k-=1 
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
print("         HACKTOBERFEST")
for i in range(s,-1,-1):
    for j in range(k+1,0,-1):
        print(end=" ")
    k+=1 
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
