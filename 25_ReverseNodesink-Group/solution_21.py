# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(begin, end):
            """
            reverse the linkedlist between (begin, end), exclusively
            """
            last = begin.next
            cur = begin.next.next
            while cur != end:
                last.next = cur.next
                cur.next = begin.next
                begin.next = cur
                cur = last.next
            last.next = end
            return last
        
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                begin = reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummy.next

