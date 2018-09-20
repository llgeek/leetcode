"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def __init__(self):
        self.next = None

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        child = head.child
        next_ = head.next
        prev = head.prev
        if not child and not next_:
            if self.next:
                head.next = self.next
                self.next.prev = head
            self.next = head
            return head
        self.flatten(next_)
        self.flatten(child)
        head.next = self.next
        self.next.prev = head
        head.child = None

        self.next = head
        return head
