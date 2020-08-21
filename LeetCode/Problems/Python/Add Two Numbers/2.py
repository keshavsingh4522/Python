# https://leetcode.com/problems/add-two-numbers/

'''
Runtime: 104 ms, faster than 25.05% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.8 MB, less than 71.64% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        m=1
        while l1 or l2:
            c=l1.val if l1 else 0
            c+=l2.val if l2 else 0
            c+=carry
            carry=c//10
            if m:
                l=ListNode(c%10)
                ptr=l
                m=0
                
            else:
                ptr.next=ListNode(c%10)
                ptr=ptr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            ptr.next=ListNode(carry)
            ptr=ptr.next
        return l
            