# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        def helper(num):
            if num == 0:
                return None
            if num == 1:
                root = TreeNode(self.head.val)
                self.head = self.head.next
                return root
            left = helper(num//2)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            right = helper(num - num//2 - 1)
            root.left = left
            root.right = right
            return root

        num = 0
        tmphead = head
        while tmphead:
            num += 1
            tmphead = tmphead.next
        return helper(num)