"""
time complexity O(N)
"""


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
        dummy = ListNode(head.val-1)
        dummy.next = head
        pre, init, cur = dummy, head, head.next
        while cur:
            if init.val != cur.val:
                pre.next = init
                pre = init
                init = cur
                cur = cur.next
            else:
                while cur and init.val == cur.val:
                    cur = cur.next
                if not cur:
                    pre.next = None
                    return dummy.next
                init = cur
                cur = cur.next
        pre.next = init
        return dummy.next
                
                