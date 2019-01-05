class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i, j = 0, 0
        m, n = len(start), len(end)
        if m != n:
            return False
        while i <= m and j <= n:
            while (i < m and start[i] == 'X'): i += 1
            while (j < n and end[j] == 'X'): j += 1
            if i == m and j == n:
                return True
            if i == m or j == n:
                return False
            if (start[i] == 'L' and end[j] == 'L' and i >= j) or \
                (start[i] == 'R' and end[j] == 'R' and i <= j):
                i += 1
                j += 1
            else:
                return False 
        return True

        
if __name__ == "__main__":
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    sol = Solution()
    print(sol.canTransform(start, end))
