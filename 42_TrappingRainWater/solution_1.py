class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        for i in range(len(height)):
            if i == 0:
                leftmax[i] = height[i]
            else:
                leftmax[i] = max(height[i], leftmax[i-1])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rightmax[i] = height[i]
            else:
                rightmax[i] = max(height[i], rightmax[i+1])
        res = 0
        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res