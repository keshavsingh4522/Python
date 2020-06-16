for _ in range(int(input())):
    n=int(input())
    q=list(map(int,input().split()))   
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            bribes=0
            break
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    if bribes!=0:
        print(bribes)