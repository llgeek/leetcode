class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        def minvalandidx(l):
            minval, idx = float('inf'), -1
            for i, val in enumerate(l):
                if val < minval:
                    minval = val
                    idx = i
            return minval, idx

        def helper(kstones, K):
            if len(kstones) == K:
                return sum(kstones)
            kacc = []
            accsum = sum(kstones[0:K-1])
            for i in range(K-1, len(kstones)):
                accsum += kstones[i]
                kacc.append(accsum)
                accsum -= kstones[i-K+1]
            minval, idx = minvalandidx(kacc)
            tmpsum = sum(kstones[idx:idx+K])
            kstones = kstones[:idx] + kstones[idx+K:]
            kstones.insert(idx, tmpsum)
            return minval + helper(kstones, K)
        
        if len(stones) == 1:
            return 0
        if (len(stones)-1)//(K-1)*(K-1) != len(stones)-1:
            return -1
        return helper(stones, K)

        # res = 0
        # minsteps = (stones-1)//(K-1)
        # kstones = stones[::-1]
        # kacc = []
        # accsum = sum(stones[0:K-1])
        # for i in range(K-1, len(stones)):
        #     accsum += stones[i]
        #     kacc.append(accsum)
        #     accsum -= stones[i-K+1]
        # for i in range(minsteps):
        #     minval, idx = minvalandidx(kacc)
        #     res += minval
        #     tmpsum = sum(kstones[idx:idx+K])
        #     kstones = kstones[:idx] + kstones[idx+K:]
        #     kstones.insert(idx, tmpsum)
        #     # kacc.pop(idx)
        #     accsum = sum(kstones[max(0, idx-K+1):idx])
        #     for k in range(max(0, idx-K+1), min(len(kacc), idx+K)):
        #         accsum += kstones[]
        #         kacc[k] = sum()

if __name__ == "__main__":
    # stones = [3, 7, 2, 3]
    # K = 2
    stones = [3, 2, 4, 1]
    K = 2
    sol = Solution()
    print(sol.mergeStones(stones, K))
