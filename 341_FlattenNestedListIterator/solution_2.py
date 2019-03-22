"""
third trial
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteg
        """
        self.stack = []
        for val in nestedList[::-1]:
            self.stack.append(val)


    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            lastval = self.stack[-1]
            if lastval.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(lastval.getList()[::-1])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
