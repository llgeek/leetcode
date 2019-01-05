"""
O(max(len(l1), len(l2))) time complexity

"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummynode = ListNode(0)
        root, cur = dummynode, dummynode
        carry = 0
        while l1 and l2:
            tmpval = l1.val + l2.val + carry
            carry, divval = divmod(tmpval, 10)
            cur.next = ListNode(divval)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            l2 = l1
        while l2:
            tmpval = l2.val + carry
            carry, divval = divmod(tmpval, 10)
            cur.next = ListNode(divval)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
        return root.next



            

        

