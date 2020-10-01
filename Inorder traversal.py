class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
# inorder tree traversal 
def printInorder(root): 
  
    if root:  
        printInorder(root.left)  
        print(root.val),  
        printInorder(root.right) 
  
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

print "\nInorder traversal of binary tree is"
printInorder(root) 
