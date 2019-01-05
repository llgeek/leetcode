"""
time complexity O(n)
space complexity O(1)

"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxarea = -1
        while i < j:
            if height[i] < height[j]:
                maxarea = max(maxarea, height[i] * (j-i))
                i += 1
            else:
                maxarea = max(maxarea, height[j] * (j-i))
                j -= 1
        return maxarea


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    print(sol.maxArea(height))
                

