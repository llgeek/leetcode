"""
follow up, how to add two numbers without reversing the lists

the basic idea is to use recursion.
recursively add the two digits from the end to the start
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
        def countListLength(head):
            cnt = 0
            while head:
                head = head.next
                cnt += 1
            return cnt
        
        def 

        len1, len2 = countListLength(l1), countListLength(l2)
        if len1 < len2:
            len1, len2 = len2, len1
            l1, l2 = l2, l1
        diff = len1 - len2
