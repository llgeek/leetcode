class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = height[0], height[-1]
        while left < right:
          if height[left] < height[right]:
            if height[left] < left_max:
              ans += left_max - height[left]
            else:
              left_max = height[left]
            left += 1
          else:
            if height[right] < right_max:
              ans += right_max - height[right]
            else:
              right_max = height[right]
            right -= 1
        return ans