N=int(input())
k1=1
if N in range(2,101):
        for i in range(1,N+1):
                for j  in range(i):
                        k1+=1
        k2=2*(k1-1)-N+1
        k1=1
        for i in range(N):
                print('*'*(2*i),sep="",end='')
                for j in range(N-i):
                        print(k1,end='0')
                        k1+=1
                for j in range(N-i):
                        if j==(N-i-1):
                                print(k2,end='')
                        else:
                                print(k2,end='0')
                        k2+=1
                k2=k2-1-2*(N-i-1)
                print()

'''
output:
5
102030405026027028029030
**6070809022023024025
****10011012019020021
******13014017018
********15016
'''
