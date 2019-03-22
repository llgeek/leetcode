from collections import Counter


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # A.sort()
        # res = 0
        # maxneg = -float('inf')
        # for i in range(len(A)):
        #     if K == 0:
        #         break
        #     if A[i] < 0:
        #         maxneg = max(maxneg, A[i])
        #         res -= A[i]
        #         K -= 1
        #     elif A[i] == 0:
        #         K -= 1

        cnt = Counter(A)
        res = 0
        maxneg = -float('inf')
        # print(cnt)
        for i in range(-100, 0):
            if i in cnt:
                maxneg = i
                if cnt[i] <= K:
                    res -= i * cnt[i]
                    K -= cnt[i]
                else:
                    res -= i * K
                    res += i * (cnt[i] - K)
                    K = 0
        if K % 2:
            if 0 in cnt:
                K = 0
            else:
                K = 1
        else:
            K = 0
        # print(maxneg)
        for i in range(1, 101):
            if i in cnt:
                if K:
                    if maxneg != -float('inf') and -maxneg < i:
                        res += 2*maxneg
                        res += i * cnt[i]
                    else:
                        res -= i
                        res += i * (cnt[i]-1)
                    K = 0
                else:
                    res += i * cnt[i]
        return res
