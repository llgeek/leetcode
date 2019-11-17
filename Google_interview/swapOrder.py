"""
Given nums:  [a1,a2,a3,...,an,b1,b2,b3,...,bn]
return nums: [a1,b1,a2,b2,...,an,bn] in place

eg:
given [1,3,5,2,4,6], return [1,2,3,4,5,6].

"""

class Solution():
  def swapOrder(self, nums):
    if not nums: return nums
    # nums[::2], nums[1::2] = nums[:(len(nums)+1)//2], nums[(len(nums)+1)//2:]
    n = len(nums[::2])
    nums[::2], nums[1::2] = nums[:n], nums[n:]

  def swapOrder2(self, nums):
    if len(nums) <= 2: return nums
    j = (len(nums)+1)//2
    n = 0
    for i in range(1, len(nums), 2):
      tmp = nums[j]
      for k in range(j, i, -1):
        nums[k] = nums[k-1]
        n += 1
      nums[i] = tmp
      j += 1
    print(n)

if __name__ == "__main__":
    sol = Solution()
    # nums = [1,3,5,2,4,6, 7]
    nums = list(range(100))
    sol.swapOrder(nums)
    print(nums)