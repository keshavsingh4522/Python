def Insert(root,data):
    if root is None:
        root=node(data)
    else:
        if root.data < data:
            if root.right is None:
                root.right=node(data)
            else:
                Insert(root.right,data)
        else:
            if root.left is None:
                root.left=node(data)
            else:
                Insert(root.left,data)