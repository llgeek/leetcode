from typing import List  
class Solution:
    def KSum(self, nums: List[int], K, target, startidx, endidx) -> List[int]:
        if K == 2:
            res = []
            i, j = startidx, endidx 
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j+1] == nums[j]:
                        j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                    while i < j and nums[j+1] == nums[j]:
                        j -= 1
                else:
                    i += 1
                    while i < j and nums[i-1] == nums[i]:
                        i += 1
            return res
        else:
            res = []
            for i in range(startidx, endidx-1):
                if i != startidx and nums[i] == nums[i-1]:
                    continue
                for subres in self.KSum(nums, K-1, target-nums[i], i+1, len(nums)-1):
                    res.append([nums[i]] + subres)
            return res
            
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.KSum(nums, 3, 0, 0, len(nums)-1)
    

if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0]
    
    sol = Solution()
    print(sol.threeSum(nums))