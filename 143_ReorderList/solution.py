# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        tmp = head
        stack = []
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        half = (len(stack) - 1) // 2
        while half != 0:
            last = stack.pop()
            half -= 1
            last.next = head.next
            head.next = last
            head = last.next
        stack.pop().next = None

