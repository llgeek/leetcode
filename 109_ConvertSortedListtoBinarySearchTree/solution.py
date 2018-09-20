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
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getMidNode(head):
            n = 0
            node = head
            while node:
                n += 1
                node = node.next
            if n == 1:
                return None, head, None
            node = head
            for i in range(1, n//2):
                node = node.next
            mid = node.next
            node.next = None
            return head, mid, mid.next if mid else None
        
        if not head:
            return None
        left, mid, right = getMidNode(head)
        root = TreeNode(mid.val)
        if left:
            leftroot = self.sortedListToBST(left)
            root.left = leftroot
        if right:
            rightroot = self.sortedListToBST(right)
            root.right = rightroot
        return root

    
    
