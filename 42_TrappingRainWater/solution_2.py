from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left = [None] * len(height)
        right = [None] * len(height)
        left[0] = 0
        right[-1] = len(height) - 1
        for i in range(1, len(height)):
            left[i] = i if height[left[i-1]] <= height[i] else left[i-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = i if height[right[i+1]] <= height[i] else right[i+1]
        res = 0
        for i in range(len(height)):
            res += min(height[left[i]], height[right[i]]) - height[i]
        return res


if __name__ == "__main__":
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))
