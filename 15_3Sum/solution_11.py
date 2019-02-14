"""
use dict, no need for sort
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        pos, neg, cnt = [], [], {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
                if num >= 0:
                    pos.append(num)
                else:
                    neg.append(num)
        res = []
        if cnt.get(0, 0) >= 3:
            res.append([0,0,0])
        for p in pos:
            for n in neg:
                rest = 0 - p - n 
                if rest in cnt:
                    if rest > p or rest < n:
                        res.append([rest, n, p])
                    elif (rest == p or rest == n) and cnt[rest] >= 2:
                        res.append([rest, n, p])
        return res



