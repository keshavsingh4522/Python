# https://leetcode.com/problems/add-two-numbers/
'''
Runtime: 88 ms, faster than 38.84% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 33.63% of Python3 online submissions for Add Two Numbers.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c=0
        k=0
        while l1:
            c=c+l1.val*(10**k)
            k+=1
            l1=l1.next
        c1=0
        k=0
        while l2:
            c1=c1+l2.val*(10**k)
            k+=1
            l2=l2.next
        c+=c1
        l=ListNode(c%10)
        c//=10
        ptr=l
        while c:
            ptr.next=ListNode(c%10)
            c//=10
            ptr=ptr.next
        return l