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
        x = {'header': head}
        def sortedListToBSTHelper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            leftroot = sortedListToBSTHelper(start, mid-1)
            root = TreeNode(x['header'].val)
            root.left = leftroot

            x['header'] = x['header'].next
            rightroot = sortedListToBSTHelper(mid+1, end)
            root.right = rightroot
            return root


        end = 0
        node = head
        while node:
            end += 1
            node = node.next
        return sortedListToBSTHelper(0, end-1)
