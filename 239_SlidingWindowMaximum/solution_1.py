from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not k or not nums or k > len(nums):
            return []
        queue = deque()
        res = [None] * (len(nums) - k + 1)
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i - k + 1 >= 0:
                res[i-k+1] = nums[queue[0]]
        return res
