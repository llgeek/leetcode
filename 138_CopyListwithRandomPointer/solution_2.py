"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        cur = dummy
        head_copy = head
        while head:
            cur.next = Node(head.val)
            cur = cur.next
            head.copy = cur
            head = head.next
        cur = dummy
        head = head_copy
        while head:
            cur.next.random = head.random.copy if head.random else None
            head = head.next
            cur = cur.next
        return dummy.next




