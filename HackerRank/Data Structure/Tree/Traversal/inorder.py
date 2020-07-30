def display(head):
    if head:
        display(head.left)
        print(head.data)
        display(head.right)