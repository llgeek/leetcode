from typing import List  
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg = {}, {}
        for val in nums:
            if val < 0:
                neg[val] = neg.get(val, 0) + 1
            else:
                pos[val] = pos.get(val, 0) + 1
        res = []
        if pos.get(0, 0) >= 3:
            res.append([0,0,0])
        for p in pos.keys():
            for n in neg.keys():
                t = 0 - p - n
                if (t == n and neg[t] >= 2) or (t < n and t in neg):
                    res.append([t, n, p])
                elif (t == p and pos[t] >= 2) or (t > p and t in pos):
                    res.append([t, n, p])
        return res
    
if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0]
    sol = Solution()
    print(sol.threeSum(nums))