# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
def levelOrder(root):
    queue=[root]
    while queue:
        print(queue[0].data,end=' ')
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue.pop(0)