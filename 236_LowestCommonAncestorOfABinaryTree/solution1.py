"""
Find pointer to each node's parent node

DFS

O(n) time complexity
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q


# def stringToTreeNode(input):
#     input = input.strip()
#     input = input[1:-1]
#     if not input:
#         return None

#     inputValues = [s.strip() for s in input.split(',')]
#     root = TreeNode(int(inputValues[0]))
#     nodeQueue = [root]
#     front = 0
#     index = 1
#     while index < len(inputValues):
#         node = nodeQueue[front]
#         front = front + 1

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             leftNumber = int(item)
#             node.left = TreeNode(leftNumber)
#             nodeQueue.append(node.left)

#         if index >= len(inputValues):
#             break

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             rightNumber = int(item)
#             node.right = TreeNode(rightNumber)
#             nodeQueue.append(node.right)
#     return root


# a = '[3,5,1,6,2,0,8,null,null,7,4]'
# p = '[5]'
# q = '[1]'

# root = stringToTreeNode(a)
# p = stringToTreeNode(p)
# q = stringToTreeNode(q)
# sol = Solution()
# sol.lowestCommonAncestor(root, p, q)
