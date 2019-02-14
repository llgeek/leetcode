

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                nextval = l1.val
                l1 = l1.next
            else:
                nextval = l2.val
                l2 = l2.next
            res.next = ListNode(nextval)
            res = res.next
        p = l1 if l1 else l2
        while p:
            res.next = ListNode(p.val)
            res = res.next
            p = p.next
        return dummy.next

