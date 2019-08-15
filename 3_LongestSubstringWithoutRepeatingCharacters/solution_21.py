class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        charidx = {}
        left = 0
        for right, c in enumerate(s):
            if c in charidx and charidx[c] >= left:
                left = charidx[c] + 1
            charidx[c] = right
            ans = max(ans, right-left+1)
        return ans