def preorder(head):
    if head:
        print(head.data)
        preorder(head.left)
        preorder(head.right)