n=int(input())
for j in range(2):
    for i in range(n):
        print(' '*(n-i-1),end='')
        print('/',end='')
        if i==1:
            print(' '*(2*i),end='')
        if i>=2:
            print(' ','/',' '*((i-2)*2),'\\',' ',end='',sep='')
        print('\\')
    for i in range(n):
        print(' '*(i+2),'\\',sep='',end='')
        if i<=n-3:
            print(' ','\\',' '*(n-3-i)*2,'/',' ','/',sep='')
        else:
            print(' '*(n-1-i)*2,'/',sep='')
    n+=1
'''
3
  /\
 /  \
/ /\ \
  \ \/ /
   \  /
    \/
   /\
  /  \
 / /\ \
/ /  \ \
  \ \  / /
   \ \/ /
    \  /
     \/
'''
