"""
use stack to pre-order traversal the tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def convertBSTtoDoubledLinkedList(self, root):
        if not root:
            return root
        head = Node(-float('inf'))
        curnode = head
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            curnode.right = node
            node.left = curnode
            curnode = node
            node = node.right
            
        head.right.left = curnode
        curnode.right = head.right
        return head.right


def buildBST(array, left, right):
    rootidx = (left + right) // 2
    if array[rootidx] == None:
        return None
    root = Node(array[rootidx])
    if left == right:
        return root
    root.left = buildBST(array, left, rootidx-1)
    root.right = buildBST(array, rootidx+1, right)
    return root

def printDoubledLiknedList(head):
    sucessororder = [head.val]
    predecessororder = []
    tmphead = head.right
    while tmphead != head:
        sucessororder.append(tmphead.val)
        tmphead = tmphead.right
    print(sucessororder)


if __name__ == "__main__":
    array = [1,2,3,4,None, 5, None]
    root = buildBST(array, 0, len(array)-1)
    sol = Solution()
    head = sol.convertBSTtoDoubledLinkedList(root)
    printDoubledLiknedList(head)
    

        
