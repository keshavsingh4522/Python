# Reverse array in groups ---> Amazon
#  Difficulty: Basic   Marks: 1
'''
Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines of input. The first line of each test case consists of an integer N(size of array) and an integer K separated by a space. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each test case, print the modified array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018

Example:
Input
2
5 3
1 2 3 4 5
6 2
10 20 30 40 50 60

Output
3 2 1 5 4
20 10 40 30 60 50

Explanation:
Testcase 1: Reversing groups in size 3, first group consists of elements 1, 2, 3. Reversing this group, we have elements in order as 3, 2, 1.
'''
from math import ceil
for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr[:k]=arr[k-1::-1] #i was having a bit difficulty in converting the first group inside the loop
    for i in range(1,ceil(float(n)/k)):
        arr[k*i:k*i+k]=arr[k*i+k-1:k*i-1:-1]
    print(*arr)
'''for _ in range(int(input())):
    n1,n2=input().split()
    a=list(map(int,input().split()))
#     if int(n1)%int(n2)!=0:
#         n2=int(n1)//int(n2)+1
    j=int(n1)//int(n2)
    for i in range(j):
        c=[]
        for k in range(int(n2)*i,int(n2)*(i+1)):
            c.append(a[k])
        print(*(c[::-1]),end=' ')
    print('',*(a[:int(n2)*j-1:-1]),end='',sep=' ')
    print()
'''

