# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        head = ListNode(0)
        cur = head
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return head.next