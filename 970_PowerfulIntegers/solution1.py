
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # if x == 1 and y == 1:
        #     if 2 <= bound:
        #         return [2]
        #     else:
        #         return []
        res = set()
        import math
        times = int(math.log2(bound))
        for i in range(times):
            for j in range(times):
                val = x**i + y**j
                if val <= bound:
                    res.add(val)
        return list(res)


if __name__ == "__main__":
    x = 1
    y = 2
    bound = 100
    sol = Solution()
    print(sol.powerfulIntegers(x, y, bound))
