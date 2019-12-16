from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curend, farestreach = 0, 0
        for i in range(len(nums)-1):
            farestreach = max(farestreach, i + nums[i])
            if i == curend:
                jumps += 1
                curend = farestreach
        return jumps
