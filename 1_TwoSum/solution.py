'''
O(n) time complexity
O(n) space complexity
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenum = dict()
        for idx, val in enumerate(nums):
            if target - val in seenum:
                return [seenum[target-val], idx]
            seenum[val] = idx
        return [-1, -1]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))