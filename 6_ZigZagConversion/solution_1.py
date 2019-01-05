"""
sort by rows

time complexity: O(n), space complexity O(n)
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        rowid = 0
        flag = 1
        for i in range(len(s)):
            if rowid == 0:
                flag = 1
            if rowid == numRows-1:
                flag = -1
            rows[rowid].append(s[i])
            rowid += flag
        rows = [''.join(rowstr) for rowstr in rows]
        return ''.join(rows)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 1
    sol = Solution()
    print(sol.convert(s, numRows))
