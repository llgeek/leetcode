"""
do not use extra space

for list A->B->C
store A->A'->B->B'->C->C'

O(n) time complexity, O(1) space complexity
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            nex = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nex
            cur = nex
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        dummy = RandomListNode(0)
        old, new = head, dummy
        while old:
            new.next = old.next
            new = new.next
            old.next = new.next
            old = old.next
        return dummy.next


