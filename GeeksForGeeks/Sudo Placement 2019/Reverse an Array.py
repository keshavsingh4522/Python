# Reverse an array ---> Infosys, Moonfrog Labs
#  Difficulty: School   Marks: 0
'''
Given an array A of size N, print the reverse of it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of input. First line contains N the size of the array A. The second line contains the elements of the array.

Output:
For each testcase, in a new line, print the array in reverse order.

Constraints:
1 <= T <= 100
1 <= N <=100
0 <= Ai <= 100

Example:
Input:
1
4
1 2 3 4
Output:
4 3 2 1
'''
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    print(*a)
