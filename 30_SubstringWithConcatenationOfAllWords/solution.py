from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wordset = Counter(words)
        wordlen = len(words[0])
        wordnum = len(words)
        res = []
        for start in range(wordlen):
            num = 0
            pre, cur = start, start
            wordset = Counter(words)
            while cur + wordlen <= len(s):
                word = s[cur:cur+wordlen]
                if word in wordset:
                    wordset[word] -= 1
                    num += 1
                else:
                    num = 0
                    pre = cur+wordlen
                    wordset = Counter(words)
                while wordset[word] < 0 or num > wordnum:
                    preword = s[pre:pre+wordlen]
                    wordset[preword] += 1
                    num -= 1
                    pre += wordlen
                if num == wordnum:
                    if not any(wordset.values()):
                        res.append(pre)
                    wordset[s[pre:pre+wordlen]] += 1
                    pre += wordlen
                    num -= 1
                cur += wordlen
        return res

if __name__ == "__main__":
    sol = Solution()
    # s = "barfoothefoobarman"
    # words = ["foo","bar"]
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(sol.findSubstring(s, words))

            

        