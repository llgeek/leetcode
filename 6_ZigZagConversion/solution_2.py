class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1: return s
    res = [[] for _ in range(numRows)]
    row = 0
    direct = 1
    for c in s:
      res[row].append(c)
      if row == 0:
        direct = 1
      if row == numRows-1:
        direct = -1
      row += direct
    return "".join("".join(row) for row in res)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    print(sol.convert(s, numRows))


        