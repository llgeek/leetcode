class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = {}
        for right, c in enumerate(s, 1):
            while c in cnt and cnt[c] > 0:
                cnt[s[left]] -= 1
                left += 1
            cnt[c] = cnt.get(c, 0) + 1
            ans = max(ans, right-left)
        return ans
    
if __name__ == "__main__":
    # s = "abcabcbb"
    # s = "bbbbb"
    # s =  "pwwkew"
    s = " "
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))