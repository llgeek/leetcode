"""
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window
"""

class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        cnt = {}
        prefix = 0
        left = 0
        distnum = 0
        res = 0
        for right, c in enumerate(A):
            if cnt.get(c, 0) == 0:
                distnum += 1
            cnt[c] = cnt.get(c, 0) + 1
            if distnum > K:
                cnt[A[left]] -= 1
                # if cnt[A[left]] == 0:
                distnum -= 1
                left += 1
                prefix = 0
            while cnt[A[left]] > 1:
                cnt[A[left]] -= 1
                left += 1
                prefix += 1
            if distnum == K:
                res += prefix + 1
        return res


if __name__ == "__main__":
    # A = [1, 2, 1, 2, 3]
    # K = 2
    A = [1, 2, 1, 3, 4]
    K = 3
    sol = Solution()
    print(sol.subarraysWithKDistinct(A, K))
