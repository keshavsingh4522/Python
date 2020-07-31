def inorder(head):
    if head:
        inorder(head.left)
        print(head.data)
        inorder(head.right)