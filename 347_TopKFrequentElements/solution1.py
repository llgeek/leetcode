"""
bucket sort
O(n) time complexity
"""
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        bucket = [None] * (len(nums)+1)
        res = []
        for key, value in cnt.items():
            if bucket[value] == None:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
        i = len(nums)
        while i >= 0 and len(res) < k:
            if bucket[i]:
                res.extend(bucket[i])
            i -= 1
        return res[:k]