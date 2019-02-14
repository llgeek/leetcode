"""
the straightforward idea is to use stack,
reverse the linkedlist, adding from the end to the start 

or if not use stack, we can directly reverse the link
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
        def reverseLink(head):
            pre = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while stack1 and stack2:
            val = stack1[-1] + stack2[-1] + carry
            carry, val = divmod(val, 10)
            stack1.pop()
            stack2.pop()
            curnode = ListNode(val)
            curnode.next = head
            head = curnode
        stack = stack1 if stack1 else stack2
        while stack:
            val = stack[-1] + carry
            carry, val = divmod(val, 10)
            stack.pop()
            curnode = ListNode(val)
            curnode.next = head
            head = curnode
        if carry:
            curnode = ListNode(carry)
            curnode.next = head
            head = curnode
        return head
