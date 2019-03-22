class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        left = 0
        cnt = {}
        res = -float('inf')
        for right, c in enumerate(s):
            while cnt.get(c, 0) != 0:
                cnt[s[left]] -= 1
                left += 1
            cnt[c] = 1
            res = max(res, right-left+1)
        return max(res, 0)

if __name__ == "__main__":
    # s = "abcabcbb"
    # s = 'bbbbb'
    s = 'pwwkew'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
