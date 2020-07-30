def postorder(head):
    if head:
        display(head.left)
        display(head.right)
        print(head.data)