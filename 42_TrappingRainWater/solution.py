"""
DP
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        left_max, right_max = [0] * len(height), [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        ans = 0
        i = 0
        while i < len(height):
            ans += min(left_max[i], right_max[i]) - height[i]
            i += 1
        return ans