"""
recursive way
"""
class Solution:
    def depthSum(self, nestedList):
        def getsum(inlist, depth):
            tmpsum = 0
            for val in inlist:
                if type(val) == int:
                    tmpsum += depth * val
                else:
                    tmpsum += getsum(val, depth+1)
            return tmpsum

        return getsum(nestedList, 1)
    

"""
iterative way
"""
from collections import deque
class Solution1:
    def depthSum(self, nestedList):
        if not nestedList:
            return 0
        tmpsum, level = 0, 1
        stack = deque(nestedList)
        while stack:
            length = len(stack)
            for i in range(length):
                head = stack.popleft()
                if type(head) is int:
                    tmpsum += head * level
                else:
                    # for val in head:
                    #     stack.append(val)
                    stack.extend(head)
            level += 1
        return tmpsum


if __name__ == "__main__":
    nestedList = [[1, 1], 2, [1, 1]]
    # nestedList = [1, [4, [6]]]
    # nestedList = [[[[[5]]]], [[3]], 1]
    sol = Solution1()
    print(sol.depthSum(nestedList))
