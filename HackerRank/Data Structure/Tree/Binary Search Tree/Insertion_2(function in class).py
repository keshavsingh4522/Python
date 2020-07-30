# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?h_r=next-challenge&h_v=zen
class Node:
    def __init__(self, info):
        self.data = info  
        self.left = None  
        self.right = None 
def preOrder(root):
    if root == None:
        return
    print (root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)
class BinarySearchTree:
    def __init__(self): 
        self.root = None
    def add_data(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            head=self.root
            while head:
                if head.data<data:
                    if head.right is None:
                        head.right=Node(data)
                        break
                    else:
                        head=head.right
                else:
                    if head.left is None:
                        head.left=Node(data)
                        break
                    else:
                        head=head.left
b=BinarySearchTree()
a=map(int,input('Enter data of Nodes: ').split())
for i in a:
    b.add_data(i)
preOrder(b.root)