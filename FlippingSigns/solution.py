class Solution:
    def flipSigns(self, s, k):
        numop = 0
        l = len(s)
        bins = list(map(lambda x: int(x=='+'), s))
        for i in range(l-k+1):
            if not bins[i]:
                for j in range(k):
                    bins[i+j] = (bins[i+j] + 1) % 2
                numop += 1
        return numop if all(bins) else -1

if __name__ == "__main__":
    s = '---+-++-'
    k = 3
    sol = Solution()
    print(sol.flipSigns(s, k))
