# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        queue1, queue2 = [], []
        cur1, cur2 = root1, root2
        while (queue1 or cur1) and (queue2 or cur2):
            while cur1:
                queue1.append(cur1)
                cur1 = cur1.left
            while cur2:
                queue2.append(cur2)
                cur2 = cur2.left
            if queue1[-1].val < queue2[-1].val:
                cur1 = queue1.pop()
                res.append(cur1.val)
                if cur1.right:
                    cur1 = cur1.right
                else:
                    cur1 = None
            else:
                cur2 = queue2.pop()
                res.append(cur2.val)
                if cur2.right:
                    cur2 = cur2.right
                else:
                    cur2 = None
        remain_queue, remain_cur = (queue1, cur1) if (queue1 or cur1) else (queue2, cur2)
        while remain_queue or remain_cur:
            while remain_cur:
                remain_queue.append(remain_cur)
                remain_cur = remain_cur.left
            remain_cur = remain_queue.pop()
            res.append(remain_cur.val)
            if remain_cur.right:
                remain_cur = remain_cur.right
            else:
                remain_cur = None
        return res