class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                ans = max(ans, (i - stack[-1] -1) * heights[idx])
            stack.append(i)
        return ans
