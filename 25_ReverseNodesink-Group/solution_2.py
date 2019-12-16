# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        knext = head
        for i in range(k):
            if not knext:
                return head
            knext = knext.next
        cur = head
        pre = head
        cur = self.reverseKGroup(knext, k)
        for i in range(k):
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur
