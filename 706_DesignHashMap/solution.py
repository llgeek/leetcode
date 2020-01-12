class LinkedNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 10000
        self.head = [None] * self.m
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.m
        if self.head[idx] is None:
            self.head[idx] = LinkedNode(key, value)
        else:
            curnode = self.head[idx]
            while True:
                if curnode.pair[0] == key:
                    curnode.pair = (key, value)
                    return
                if curnode.next is None:
                    break
                curnode = curnode.next
            curnode.next = LinkedNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.m
        if self.head[idx] is None:
            return -1
        curnode = self.head[idx]
        while curnode:
            if curnode.pair[0] == key:
                return curnode.pair[1]
            curnode = curnode.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.m
        if self.head[idx] is None:
            return
        curnode = self.head[idx]
        if curnode.pair[0] == key:
            self.head[idx] = curnode.next
            return
        while curnode:
            if curnode.next and curnode.next.pair[0] == key:
                curnode.next = curnode.next.next
                return
            curnode = curnode.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)