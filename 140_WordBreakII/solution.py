"""
solution1 TLE

optimize with memory
"""
from typing import List
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        wordlens = set([len(word) for word in wordDict])
        memo = defaultdict(lambda: [])
        def helper(idx):
            if idx >= len(s):
                return []
            if idx in memo:
                return memo[idx]
            if s[idx:] in wordset:
                memo[idx].append(s[idx:])
            for poslen in wordlens:
                j = idx + poslen - 1
                if s[idx: j+1] in wordset:
                    for path in helper(j+1):
                        memo[idx].append(s[idx: j+1] + ' ' + path)
            return memo[idx]
        return helper(0)
            


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        wordlens = set([len(word) for word in wordDict])
        res = []
        def helper(path, idx):
            if idx >= len(s):
                if path:
                    res.append(path)
                return
            for poslen in wordlens:
                j = idx + poslen - 1
                if j < len(s) and s[idx:j+1] in wordset:
                    helper(path + [s[idx:j+1]], j+1)
        helper([], 0)
        return [" ".join(sentence) for sentence in res]


if __name__ == "__main__":
    sol = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(sol.wordBreak(s, wordDict))