class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        current = 0
        while current < len(height):
          while stack and height[stack[-1]] < height[current]:
            top = stack.pop()
            if not stack:
              break
            dist = current - stack[-1] - 1
            boundheight = min(height[stack[-1]], height[current]) - height[top]
            ans += dist * boundheight
          stack.append(current)
          current += 1
        return ans