"""
second trial
"""


class Solution:
    def kSum(self, nums, k, start, end, target):
        if k == 2:
            res = []
            i, j = start, end
            while i < j:
                tmpsum = nums[i] + nums[j]
                if tmpsum == target:
                    res.append([nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif tmpsum > target:
                    j -= 1
                else:
                    i += 1
            return res
        else:
            res = []
            for i in range(start, end-k+2):
                if i != start and nums[i] == nums[i-1]:
                    continue
                ret = self.kSum(nums, k-1, i+1, end, target-nums[i])
                for tmpres in ret:
                    res.append([nums[i]] + tmpres)
            return res
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        return self.kSum(nums, 3, 0, len(nums)-1, 0)

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))
