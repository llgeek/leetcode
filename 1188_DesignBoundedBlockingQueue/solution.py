import theading
from collections import deque
class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.semaphore = threading.Semaphore()
        self.capacity = capacity
        self.deque = deque()

    def enqueue(self, element):
        pass

    def dequeue(self):
        pass

    def size(self):
        pass