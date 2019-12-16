"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0, None, None)
        cur = dummy
        curhead = head
        while curhead:
            cur.next = Node(curhead.val, None, None)
            cur = cur.next
            curhead.copy = cur
            curhead = curhead.next
        curhead = head
        cur = dummy.next
        while curhead:
            if curhead.random:
                cur.random = curhead.random.copy
            cur = cur.next
            curhead = curhead.next
        return dummy.next

