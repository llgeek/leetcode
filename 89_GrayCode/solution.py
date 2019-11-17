from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
          res += [(1<<i) + x for x in res[::-1]]
        return res

if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.grayCode(n))