"""
go 2 passes

first pass, compare the candidate with other people,
start from initial candidate res, compare it with other people
if res knows i, then set res = i. (candidate before i cannot be candidate because at least res does not know them)

sencod pass, check whether res is the true celebrity
"""

class Solution():
    def findCelebrity(self, n):
        res = 0
        for i in range(1, n):
            if knows(res, i):
                res = i
        for i in range(n):
            if i != res and (knows(res, i) or not knows(i, res)): return -1
        return res