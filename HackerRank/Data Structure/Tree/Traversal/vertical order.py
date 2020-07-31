def vertical(head,hd,m):
    if head is None:
        return
    if hd not in m:
        m[hd]=head.data
    vertical(head.left,hd-1,m)
    vertical(head.right,hd+1,m)
m=dict()
hd=0
vertical(root,hd,m)
for i in sorted(m):
    print(m[i][0])