# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      heap = []
      for idx, node in enumerate(lists):
        if node:
          heapq.heappush(heap, (node.val, idx, node))
      head = ListNode(0)
      cur = head
      while heap:
        val, idx, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        node = node.next
        if node:
          heapq.heappush(heap, (node.val, idx, node))
      return head.next
      
        