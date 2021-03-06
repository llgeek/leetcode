"""
TLE in leetcode

"""

class Solution:
    CAPACITY = float('inf')

    def shipWithinDays(self, weights, D: int) -> int:
        def helper(idx, day, cap):
            if day > D or cap > self.CAPACITY:
                return
            if idx >= len(weights):
                self.CAPACITY = cap
                return
            i = idx
            tmpsum = 0
            while i < len(weights) and tmpsum <= cap:
                tmpsum += weights[i]
                i += 1
            if tmpsum <= cap:
                helper(i, day+1, cap)
            else:
                helper(i-1, day+1, cap)
                while i < len(weights):
                    helper(i, day+1, tmpsum)
                    tmpsum += weights[i]
                    i += 1
        total = sum(weights)
        maxwei = max(weights)
        
        helper(0, 0, max(int(total/D), maxwei))
        return self.CAPACITY

if __name__ == "__main__":
    # weights = [180, 373, 75, 82, 497, 23, 303, 299, 53, 426, 152, 314, 206,
    #     433, 283, 370, 179, 254, 265, 431, 453, 17, 189, 224]
    # D = 12
    # weights = [361, 321, 186, 186, 67, 283, 36, 471, 304, 218, 60, 78, 149, 166,
    #            282, 384, 61, 242, 426, 275, 236, 221, 27, 261, 487, 90, 468, 19, 453, 241]
    # D = 15
    weights = [200,412,270,110,407,253,219,402,75,271,111,279,291,418,36,320,71,200,7,377,216,261,20,153,193,399,363,186,395,63,352,8,38,334,152,322,134,337,326,72,475,157,491,420,21,188,127,249,61,314,218,351,229,37,103,213,380,398,112,221,332,85,65,368,87,29,320,366,346,137,3,414,77,228,14,225,233,50,329,291,384,469,67,377,213,49,490,465,269,316,200,60,159,275,183,311,441,199,343,227,29,153,283,145,493,83,395,486,23,488,445,192,38,268,363,132,31,225,30,126,240,223,367,400,425,209,300,351,334,278,263,267,458,165,144,112,271,398,131,132,112,15,343,90,178,3,353,274,75,210,309,382,342,162,219,383,8,404,356,374,61,437,115,216,21,498,64,474,348,45,208,110,471,445,215,328,272,434,89,293,285,103,406,420,137,22,30,52,6,307,353,278,126,113,384,421,111,243,54,162]
    D = 100
    sol = Solution()
    print(sol.shipWithinDays(weights, D))
