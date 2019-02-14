"""
recursively call pre-order tree traversal
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None
        self.pre = None
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.pre:
            self.head = root
        else:
            self.pre.right = root
            root.left = self.pre
        self.pre = root
        self.inorder(root.right)

    def convertBSTtoDoubledLinkedList(self, root):
        if not root:
            return None
        self.inorder(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


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
    array = [1, 2, 3, 4, None, 5, None]
    root = buildBST(array, 0, len(array)-1)
    sol = Solution()
    head = sol.convertBSTtoDoubledLinkedList(root)
    printDoubledLiknedList(head)
