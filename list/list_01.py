if __name__ == '__main__':
    # take input as a number
    N = int(input())
    # define two lists
    z=[]
    l=[]
    for i in range(N):
        # add some input to the end of list z
        z.append(input())
    for x in z:
        y=x.split()
        if y[0]=='insert':
            # insert the secound argument at the index of the secound argument
            l.insert(int(y[1]),int(y[2]))
        if y[0]=='append':
            # add to the end of the list
            l.append(int(y[1]))
        if y[0]=='remove':
            try:
                # removes the first item from the list that equaled int(y[1])
                l.remove(int(y[1]))
            except:
                pass
        if y[0]=='print':
            print(l)
        if y[0]=='sort':
            l.sort()
        if y[0]=='reverse':
            # reverse the order of the list
            l.reverse()
        if y[0]=='pop':
            try:
                # delete the last item
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
