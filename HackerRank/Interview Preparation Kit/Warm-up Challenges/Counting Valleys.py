n=int(input())
a=input()
see_level=0
count=0
for i in a:
    if i=='U':
        see_level+=1
    else:
        see_level-=1
    if see_level==0 and i=='U':
        count+=1
print(count)
