def postorder(head):
    if head:
        postorder(head.left)
        postorder(head.right)
        print(head.data)