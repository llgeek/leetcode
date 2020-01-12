"""
O(N^2) complexity
"""
class Solution:
    def shortest_way(self, source, target):    
        if set(source) != set(target) or not source:
            return -1

        res = 0
        i, j = 0, 0
        while j < len(target):
            while i < len(source) and source[i] != target[j]:
                i += 1
            if i == len(source):
                i = 0
                res += 1
            else:
                i += 1
                j += 1
        return res + (i != 0)

if __name__ == "__main__":
    sol = Solution()
    source = "abc"
    target = "abcbc"
    source = "abc"
    target = "acdbc"
    source = "xyz"
    target = "xzyxz"
    print(sol.shortest_way(source, target))

