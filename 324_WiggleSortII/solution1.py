"""
partition based idea

findKthLargest will make sure the left side are greater than value at k-1, and right side are smaller than value at k-1
"""


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(nums, start, end):
            i = start-1
            for j in range(start, end+1):
                if nums[j] > nums[end]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[end] = nums[end], nums[i]
            return i


        
        def findKthLargest(nums, k):
            import random
            rnd = random
            for i in range(len(nums)):
                j = rnd.randint(0, len(nums)-1)
                nums[i], nums[j] = nums[j], nums[i]
            
            left, right = 0, len(nums)-1
            mid = right
            k -= 1
            while left < right:
                mid = partition(nums, left, right)
                if mid < k:
                    left = mid+1
                elif mid > k:
                    right = mid-1
                else:
                    break
            return nums[k]
        
        mapIDx = lambda x: (2*x+1) % (len(nums) | 1)

        midval = findKthLargest(nums, (len(nums)+1)//2)
        print(nums)
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[mapIDx(i)] < midval:
                nums[mapIDx(right)], nums[mapIDx(i)] = nums[mapIDx(i)], nums[mapIDx(right)]
                right -= 1 
            elif nums[mapIDx(i)] > midval:
                nums[mapIDx(left)], nums[mapIDx(i)] =  nums[mapIDx(i)], nums[mapIDx(left)]
                left += 1
                i += 1
            else:
                i += 1
        



if __name__ == "__main__":
    # nums = [1,5,1,1,6,4]
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [1]
    nums = [5, 3, 1, 2, 6, 7, 8, 5, 5]
    sol = Solution()
    sol.wiggleSort(nums)
    print(nums)


