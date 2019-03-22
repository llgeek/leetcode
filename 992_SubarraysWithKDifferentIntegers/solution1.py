class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K-1)

    def atMostK(self, A, K):
        left = 0
        cnt = {}
        distinctnum = 0
        res = 0
        for right, c in enumerate(A):
            if cnt.get(c, 0) == 0:
                distinctnum += 1
            cnt[c] = cnt.get(c, 0) + 1
            while distinctnum > K:
                cnt[A[left]] -= 1
                if cnt[A[left]] == 0:
                    distinctnum -= 1
                left += 1
            res += (right-left+1)
        return res

if __name__ == "__main__":
    # A = [1, 2, 1, 2, 3]
    # K = 2
    A = [1, 2, 1, 3, 4]
    K = 3
    sol = Solution()
    print(sol.subarraysWithKDistinct(A, K))
            


