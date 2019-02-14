# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head.next
        pre = head
        preval = head.val
        while cur:
            if cur.val == preval:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                preval = cur.val
                cur = cur.next
        return head

