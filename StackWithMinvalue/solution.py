"""
we can use two stack to implement this

data stack: store actual values
min stack: store the minimal value
"""
class Stack:
    def __init__(self, capacity = 500):
        self.capacity = capacity
        self.curidx = -1
        self.data = [-1] * capacity
    
    def isEmpty(self):
        return self.curidx == -1

    def isFull(self):
        return self.curidx == self.capacity - 1

    def push(self, val):
        if self.isFull():
            exit('stack is full')
        self.curidx += 1
        self.data[self.curidx] = val
    
    def pop(self):
        if self.isEmpty():
            exit('stack is empty')
        self.curidx -= 1
        return self.data[self.curidx+1]


class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.min = Stack()
    
    def push(self, val):
        super().push(val)
        if self.min.isEmpty():
            self.min.push(val)
        else:
            top = self.min.pop()
            self.min.push(val if val < top else top)

    def pop(self):
        self.min.pop()
        return self.data.pop()
    
    def getMin(self):
        val = self.min.pop()
        self.min.push(val)
        return val

if __name__ == "__main__":
    s = SpecialStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getMin())
    s.push(5)
    print(s.getMin())
