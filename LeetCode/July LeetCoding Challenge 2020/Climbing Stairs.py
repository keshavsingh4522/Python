'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def get_p(n,n1,n2):
    return fact(n)//(fact(n1)*fact(n2))

n=int(input())
c_2=n//2
c_1=n%2
sum_p=1
while c_2:
    sum_p+=get_p(c_2+c_1,c_2,c_1)
    c_2-=1
    c_1+=2
print(sum_p)

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        def fact(n):
            if n==0:
                return 1
            return n*fact(n-1)
        def get_p(n,n1,n2):
            return fact(n)//(fact(n1)*fact(n2))
        c_2=n//2
        c_1=n%2
        sum_p=1
        while c_2:
            sum_p+=get_p(c_2+c_1,c_2,c_1)
            c_2-=1
            c_1+=2
        return(sum_p)
'''