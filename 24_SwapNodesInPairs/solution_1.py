# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp
            cur = cur.next.next
        return dummy.next
            