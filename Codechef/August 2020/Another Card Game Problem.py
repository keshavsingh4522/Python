import math
for _ in range(int(input())):
    c,r=map(int,input().split())
    movc=math.ceil(c/9)
    movr=math.ceil(r/9)
    if movr<=movc:
        print(1,movr)
    else:
        print(0,movc)
