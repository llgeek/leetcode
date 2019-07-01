class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        seenchr = set()
        res = 0
        while right < len(s):
            if s[right] in seenchr:
                while left < right and s[left] != s[right]:
                    seenchr.discard(s[left])
                    left += 1
                if left < right:
                    seenchr.discard(s[left])
                    left += 1
            seenchr.add(s[right])
            res = max(res, right-left+1)
            right += 1
        return res
    
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seenchr = {}
        res = 0
        for i in range(len(s)):
            if s[i] in seenchr and seenchr[s[i]] > start:
                start = seenchr[s[i]] + 1
            seenchr[s[i]] = i
            res = max(res, i-start+1)
        return res
            
    
    
if __name__ == "__main__":
    # s = "pwwkew"
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
            