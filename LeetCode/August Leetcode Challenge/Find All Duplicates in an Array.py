# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
class Solution:
    def findDuplicates(self, a: List[int]) -> List[int]:
        l=[]
        for i in range(len(a)):
            if a[abs(a[i])-1]>0:
                a[abs(a[i])-1]=-a[abs(a[i])-1]
            else:
                l.append(abs(a[i]))
        return l