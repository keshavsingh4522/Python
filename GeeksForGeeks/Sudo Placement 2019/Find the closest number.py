# Find the closest number
# Difficulty: Basic   Marks: 1
'''
Given an array of sorted integers. The task is to find the closest value to the given number in array. Array may contain duplicate values.

Note: If the difference is same for two values print the value which is greater than the given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains two integers N & K and the second line contains N space separated array elements.

Output:
For each test case, print the closest number in new line.

Constraints:
1<=T<=100
1<=N<=105
1<=K<=105
1<=A[i]<=105

Example:
Input:
2
4 4
1 3 6 7
7 4
1 2 3 5 6 8 9

Output:
3
5
'''
for _ in range(int(input())):
    n1,n2=map(int,input().split())
    a=list(map(int,input().split()))
    a.append(n2)
    a.sort()
    for i in range(len(a)):
        if a[-1]==n2:
            print(a[-2])
            break
        else:
            if a[i]==n2:
                if a[i+1]==n2:
                    print(n2)
                    break
                else:
                    if abs(n2-a[i+1])==abs(n2-a[i-1]):
                        print(a[i+1])
                        break
                    else:
                        if abs(n2-a[i+1])>abs(n2-a[i-1]):
                            print(a[i-1])
                            break
                        else:
                            print(a[i+1])
                            break
