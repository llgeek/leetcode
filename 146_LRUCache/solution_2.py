class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        n = self.dict[key]
        self._remove(n)
        self._add(n)
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)
        if len(self.dict) > self.capacity:
            del self.dict[self.head.next.key]
            self._remove(self.head.next)

    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.next = self.tail
        self.tail.pre = node
        node.pre = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)