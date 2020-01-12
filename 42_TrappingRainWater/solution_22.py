from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            if left_max < height[left]:
                left_max = height[left]
            if right_max < height[right]:
                right_max = height[right]
            if left_max < right_max:
                ans += (left_max - height[left])
                left += 1
            else:
                ans += (right_max - height[right])
                right -= 1
        return ans