"""
optimize with O(1) space and time

just need to keep track of the min value,
while each time occuring a smaller value (which means we need to update min value),
we need to store a combination of previous min value and current value,
so that next time we pop the min value, we can recover the previous min value
"""


class Stack:
    def __init__(self, capacity=500):
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
        self.minval = None

    def push(self, val):
        if self.isEmpty():
            super().push(val)
            self.minval = val
        elif val < self.minval:
            super().push(2*val-self.minval)
            self.minval = val
        else:
            super().push(val)

    def pop(self):
        x = super().pop()
        if x < self.minval:
            tmp = self.minval
            self.minval = 2*self.minval - x
            x = tmp
        return x

    def getMin(self):
        if self.isEmpty():
            exit('stack is empty')
        return self.minval


if __name__ == "__main__":
    s = SpecialStack()
    # s.push(10)
    # s.push(20)
    # s.push(30)
    # print(s.getMin())
    # s.push(5)
    # print(s.getMin())
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(1)
    s.push(1)
    s.push(-1)
    print(s.data)


