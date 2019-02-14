"""
divide and conquer

recursive to join left linked list and right linked list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def join(self, left, right):
        if not left:
            return right
        if not right:
            return left
        leftlast = left.left
        rightlast = right.left
        leftlast.right = right
        right.left = leftlast
        rightlast.right = left
        left.left = rightlast
        return left

    def convertBSTtoDoubledLinkedList(self, root):
        if not root:
            return root
        left = self.convertBSTtoDoubledLinkedList(root.left)
        right = self.convertBSTtoDoubledLinkedList(root.right)
        root.left = root
        root.right = root
        return self.join(self.join(left, root), right)


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





