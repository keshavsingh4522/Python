'''

Consider the following 4×4 pattern:

 1  2  4  7
 3  5  8 11
 6  9 12 14
10 13 15 16
You are given an integer N. Print the N×N pattern of the same kind (containing integers 1 through N2).

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output
For each test case, print N lines; each of them should contain N space-separated integers.

Constraints
1≤T≤10
1≤N≤100
Subtasks
Subtask #1 (100 points): Original constraints

Example Input
1
4
Example Output
1 2 4 7
3 5 8 11
6 9 12 14
10 13 15 16

'''

for _ in range(int(input())):
    n=int(input())
    a=[[None]*n for i in range(n)]
    k=1

    for i in range(n):
        for j in range(i+1):
            a[j][i-j]=k
            k+=1

    for i in range(1,n):
        for j in range(n-i):
            a[i+j][n-1-j]=k
            k+=1
    #display
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()