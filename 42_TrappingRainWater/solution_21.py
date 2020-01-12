from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                idx = stack.pop()
                if stack:
                    res += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[idx])
            stack.append(i)
        return res
