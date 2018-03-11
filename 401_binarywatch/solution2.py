"""
DFS solution version
"""
class Solution:
    def readBinaryWatch(self, num):
        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins >= 60:
                return
            if not n:
                result.append("{:d}:{:02d}".format(hours, mins))
                return 
            for i in range(idx, 10):
                if i < 4:
                    dfs(n-1, hours | 1 << i, mins, i+1)
                else:
                    k = i - 4
                    dfs(n-1, hours, mins | 1 << k, i+1)

        result = []
        dfs(num, 0, 0, 0)
        return result

s = Solution()
print(s.readBinaryWatch(2))