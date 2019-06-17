class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        res = []
        val = {1: '1', 0:'0'}
        while N:
            rem = N % -2
            N //= -2
            if rem < 0:
                rem += 2
                N += 1
            res.append(val[rem])
        res = "".join(res[::-1]).lstrip('0')
        return res if res else '0'
            

if __name__ == "__main__":
    N = 2
    sol = Solution()
    print(sol.baseNeg2(N))
    



