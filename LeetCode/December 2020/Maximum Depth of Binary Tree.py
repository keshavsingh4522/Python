'''https://leetcode.com/explore/featured/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.height=0
    def maxDepth(self, root: TreeNode) -> int:
        def f(root,c):
            if root:
                f(root.left,c+1)
                f(root.right,c+1)
                if c>self.height:
                    self.height=c
        f(root,1)
        return self.height
