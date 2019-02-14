"""
use dict to map old node to new node

O(n) time complexity, O(n) space complexity
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
        if not head:
            return None
        m = n = head
        nodemap = dict()
        nodemap[None] = None
        while m:
            nodemap[m] = RandomListNode(m.label)
            m = m.next
        while n:
            nodemap[n].next = nodemap[n.next]
            nodemap[n].random = nodemap[n.random]
            n = n.next
        return nodemap[head]


        # if not head:
        #     return None
        # nodemap = dict()
        # old = head
        # dummy = RandomListNode(0)
        # new = dummy
        # while old:
        #     tmp = RandomListNode(old.label)
        #     new.next = tmp
        #     nodemap[old] = tmp
        #     new = tmp
        #     old = old.next
        # old = head
        # new = dummy.next
        # while old:
        #     new.random = nodemap[old.random]
        # return dummy.next


