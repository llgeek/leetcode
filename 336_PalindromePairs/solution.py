"""
TLE
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        revwords = [word[::-1] for word in words]
        res = []
        for i in range(len(words)):
          for j in range(len(words)):
            if i == j: continue
            if words[i] + words[j] == revwords[j] + revwords[i]:
              res.append([i, j])
        return res