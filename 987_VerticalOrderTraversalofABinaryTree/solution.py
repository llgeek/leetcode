# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        MAXNUM, MINNUM = (1<<31)-1, - 1<<31
        pos2val = {}
        minleft, maxright = MAXNUM, MINNUM
        maxdown = MINNUM
        stack = [(root, 0, 0)]
        while stack:
            curnode, x, y = stack.pop()
            if x < minleft: minleft = x
            elif x > maxright: maxright = x
            if y > maxdown:
                maxdown = y
            if (x, y) in pos2val:
                pos2val[x, y].append(curnode.val)
            else:
                pos2val[x, y] = [curnode.val]
            if curnode.right:
                stack.append((curnode.right, x+1, y+1))
            if curnode.left:
                stack.append((curnode.left, x-1, y+1))
        res = [[] for _ in range(maxright-minleft+1)]
        for i in range(len(res)):
            for j in range(maxdown+1):
                if (i+minleft, j) in pos2val:
                    res[i].extend(sorted(pos2val[i+minleft, j]))
        return res
