class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minval = (1<<31)-1
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(x)
            self.minval = x
            return 
        if x < self.minval:
            self.stack.append(2*x-self.minval)
            self.minval = x
        else:
            self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            exit('empty stack')
        val = self.stack.pop()
        if val < self.minval:
            self.minval = 2*self.minval - val
        

    def top(self):
        """
        :rtype: int
        """
        val = self.stack[-1]
        if val < self.minval:
            return self.minval
        else:
            return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()