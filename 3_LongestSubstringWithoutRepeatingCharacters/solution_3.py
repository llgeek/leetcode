class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr2idx = dict()
        res = 0
        left, right = 0, 0
        while right < len(s):
          if s[right] in chr2idx:
            # for i in range(left, chr2idx[s[right]]):
            #   chr2idx.pop(s[i])
            left = chr2idx[s[right]] + 1
          chr2idx[s[right]] = right
          if right - left + 1 > res:
            res = right - left + 1
          right += 1
        return res
            
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))