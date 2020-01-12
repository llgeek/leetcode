class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        left, right = [None] * len(heights), [None] * len(heights)
        left[0] = -1
        right[-1] = len(heights)
        for i in range(len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        for i in range(len(heights)-1, -1, -1):
            p = i + 1
            while p <= len(heights) - 1 and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (right[i] - left[i] - 1))
        return ans
