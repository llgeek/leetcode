class Solution:
    def kDistinctCharLen(self, s: str, k: int):
        memo = {}
        res = 0
        left, right = 0, 0
        while right < len(s):
            memo[s[right]] = right
            while len(memo) > k:
                left = memo.pop(s[left]) + 1
            res = max(res, right-left+1)
            right += 1
        return res

if __name__ == "__main__":
    s = "eceba"
    k = 2
    sol = Solution()
    print(sol.kDistinctCharLen(s, k))
