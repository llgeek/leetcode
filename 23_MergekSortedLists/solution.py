"""
Note: for python3, the heap element cannot be (node.val, node), because when node.val are same, then
heapq will compare node, while node does not support comparision!


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        dummy = ListNode(0)
        curnode = dummy
        for i, head in enumerate(lists):
            if head:
                heap.append((head.val, i, head))
        heapq.heapify(heap)
        while heap:
            val, i, nextnode = heapq.heappop(heap)
            curnode.next = nextnode
            curnode = curnode.next
            if nextnode.next:
                heapq.heappush(heap, (nextnode.next.val, i, nextnode.next))
        return dummy.next
