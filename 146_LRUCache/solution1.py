"""
O(1) time complexity for all operations

use linkedlist to store the value in cache

update linkedlist to make sure least recently used element is always in the head
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if  key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)
        
        if len(self.dict) > self.capacity:
            node = self.head.next
            self._remove(node)
            # self.dict.pop(node.key, 0)
            del self.dict[node.key]


    def _remove(self, node):
        # p, n = node.prev, node.next
        # p.next = n
        # n.prev = p
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        # self.tail.prev.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        

