from collections import Counter
class Solution:
    def reorganizeString(self, S: 'str') -> 'str':
        if not S:
            return True
        cnt = Counter(S).most_common()
        # maxnum = 0
        # maxcnt = cnt[0][1]
        # for pair in cnt:
        #     if pair[1] == maxcnt:
        #         maxnum += 1
        #     else:
        #         break
        # return 2*(maxcnt-1) + maxnum <= len(S)
        res = 