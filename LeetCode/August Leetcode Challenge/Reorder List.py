# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/
'''
13 / 13 test cases passed.                   Status: Accepted
Runtime: 108 ms
Memory Usage: 23.3 MB

Your runtime beats 50.00 % of python3 submissions.
Your memory usage beats 28.30 % of python3 submissions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d=[]
        i=0
        while head:
            d.append(head)
            i+=1
            head=head.next
        n=i
        i=1
        if n:
            d[n//2].next=None
        while i<=(n//2)-1+n%2:
            temp=d[i-1].next
            d[i-1].next=d[n-i]
            d[n-i].next=temp
            i+=1
