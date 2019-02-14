"""

use deque, make sure deque[0] stores the maximial value's index, and index deque[-1]'s value is greater than current value

monotonic queue

https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not k or not nums:
            return []
        ret = [0] * (len(nums)-k+1)
        queue = deque()
        for i in range(len(nums)):
            while queue and queue[0] < i-k+1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i-k+1 >= 0:
                ret[i-k+1] = nums[queue[0]]
        return ret 

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
