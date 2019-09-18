if __name__ == '__main__':
    N = int(input())
    z=[]
    l=[]
    for i in range(N):
        z.append(input())
    for x in z:
        y=x.split()
        if y[0]=='insert':
            l.insert(int(y[1]),int(y[2]))
        if y[0]=='append':
            l.append(int(y[1]))
        if y[0]=='remove':
            try:
                l.remove(int(y[1]))
            except:
                pass
        if y[0]=='print':
            print(l)
        if y[0]=='sort':
            l.sort()
        if y[0]=='reverse':
            l.reverse()
        if y[0]=='pop':
            try:
                l.pop()
            except:
                pass
'''
input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
