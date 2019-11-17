"""
most number characters cannot exceed len(S)/2 times

then arrange them together, and split by first half to even indexes, and second half to odd indexes
"""

from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S: return ""
        cnt = Counter(S).most_common()
        maxnum = cnt[0][1]
        if maxnum * 2 > len(S) + 1: return ""
        res = []
        for pair in cnt:
          res.extend([pair[0]] * pair[1])
        print(res)
        res[::2], res[1::2] = res[:(len(S)+1)//2], res[(len(S)+1)//2:]
        return "".join(res)
