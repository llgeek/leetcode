# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def checklength(head, k):
            cur = head
            for _ in range(k):
                if not cur:
                    return False
                cur = cur.next
            return True 

        rethead = head
        if checklength(head, k):
            pre = last = head
            head = head.next
            for i in range(k-1):
                tmp = head.next
                head.next = pre
                pre = head
                if i == k-2:
                    rethead = head
                head = tmp
            last.next = self.reverseKGroup(head, k)
        return rethead
