class Solution():
    def pourWater(self, heights, V, k):
        for i in range(V):
            leftidx, rightidx = k, k
            while leftidx > 0 and heights[leftidx] >= heights[leftidx-1]:
                leftidx -= 1
            while leftidx < k and heights[leftidx] == heights[leftidx+1]:
                leftidx += 1
            while rightidx < len(heights)-1 and heights[rightidx] >= heights[rightidx+1]:
                rightidx += 1
            while rightidx > k and heights[rightidx] == heights[rightidx-1]:
                rightidx -= 1
            if heights[leftidx] < heights[k]:
                heights[leftidx] += 1
            else:
                heights[rightidx] += 1
            
        return heights
    
if __name__ == "__main__":
    heights = [2, 1, 1, 2, 1, 2, 2]
    V = 4
    k = 3
    sol = Solution()
    print(sol.pourWater(heights, V, k))
            

