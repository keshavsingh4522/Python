'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints
* 2000<year<3000
Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August 5th 2015 was WEDNESDAY.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as cal
day={0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
n=list(map(int,input().split()))

if n[2] in range(2001,3000):
    n1=cal.weekday(n[2],n[0],n[1])
    for i in day:
        if i==n1:
            print(day[i])
'''
output:
08 05 2015
WEDNESDAY
'''
