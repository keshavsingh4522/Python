# https://www.hackerrank.com/challenges/tree-top-view/problem
def topView(root):
    def fun(node, depth, pos):
        if node is None:
            return
        fun(node.left, depth+1, pos-1)
        fun(node.right, depth+1, pos+1)
        if (pos in ans and depth<ans[pos][0]) or pos not in ans:
            ans[pos] = (depth,node)

    ans = {}
    fun(root,0,0)
    keys = sorted(ans.keys())
    for key in keys:
        print(ans[key][1].data, end = ' ')