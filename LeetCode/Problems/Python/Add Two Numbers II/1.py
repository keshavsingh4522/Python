# https://leetcode.com/problems/add-two-numbers-ii/
'''
Runtime: 140 ms, faster than 7.48% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 13.8 MB, less than 84.32% of Python3 online submissions for Add Two Numbers II.
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
            c=c*10+l1.val
            k+=1
            l1=l1.next
        c1=0
        k=0
        while l2:
            c1=c1*10+l2.val
            k+=1
            l2=l2.next
        c+=c1
        m=c
        count_digit=0
        l=[]
        while m:
            l.append(m%10)
            m//=10
            count_digit+=0
        k=len(l)-1
        while k>=0:
            if k==len(l)-1:
                ld=ListNode(l[k])
                ptr=ld
            else:
                ptr.next=ListNode(l[k])
                ptr=ptr.next
            k-=1
        try:
            return ld
        except:
            return ListNode(0)