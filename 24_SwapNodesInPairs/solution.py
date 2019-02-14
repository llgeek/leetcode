# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur, nex = dummy, head
        while nex and nex.next:
            cur.next = nex.next
            nex.next = cur.next.next
            cur.next.next = nex
            cur = nex
            nex = nex.next
        return dummy.next
