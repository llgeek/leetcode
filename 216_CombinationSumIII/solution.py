from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        only accept numbers from 1 to 9!
        """
        def backtracker(ret, k, n, path, curval):
            if n == 0 and k == 0:
                ret.append(path[:])
            elif n < 0 or k < 0 or curval > n or curval > 9:
                return
            else:
                backtracker(ret, k-1, n-curval, path+[curval], curval+1)
                backtracker(ret, k, n, path, curval+1)
        ret = []
        backtracker(ret, k, n, [], 1)
        return ret

if __name__ == "__main__":
    k = 3
    n = 9
    sol = Solution()
    print(sol.combinationSum3(k, n))