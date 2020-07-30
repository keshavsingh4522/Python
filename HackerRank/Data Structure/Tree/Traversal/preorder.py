def preorder(head):
    if head:
        print(head.data)
        display(head.left)
        display(head.right)