
import re
T=int(input())
l3=[]
if T in range(1,1001):
        for i in range(T):
                P=input()
                S=input()
                if len(P)==26 and len(S) in range(1,101)  and re.match("[a-z]*$",P) and re.match("[a-z]*$",S):
                        l4=[]
                        for j in P:
                                if j in S:
                                        l4.append(j*S.count(j))
                        l3.append(l4)
        for i in l3:
                for j in i:
                        print(j,end='')
                print()
'''
output:
2
asdfghjklpoiuytrewqzxcvbnm
gtnjk
asdfghjklqwertyuiopmnbvcxz
polj
gjktn
jlop
'''
