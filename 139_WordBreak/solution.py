from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        wordlens = set([len(word) for word in wordDict])
        dp = [False] * len(s)
        for i in range(len(s)):
            for poslen in wordlens:
                j = i - poslen + 1
                if j >= 0:
                    dp[i] = dp[i] or (dp[j-1] if j > 0 else True) and s[j:i+1] in wordset
        return dp[len(s)-1]

        
if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))