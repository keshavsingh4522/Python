#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d=dict()
        ptr=root
        def f(ptr,c):
            if ptr:
                f(ptr.left,c+1)
                try:
                    d[c].next=ptr
                    d[c]=ptr
                except:
                    d[c]=ptr
                f(ptr.right,c+1)
        f(ptr,0)
        return root
