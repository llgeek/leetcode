class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        res = 0
        left = [None] * len(heights)
        right = [None] * len(heights)
        left[0] = -1
        right[-1] = len(heights)
        for i in range(len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        for i in range(len(heights)-1, -1, -1):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
        for i in range(len(heights)):
            res = max(res, heights[i] * (right[i] - left[i] - 1))
        return res
