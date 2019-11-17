
"""
Given an array of size n containing equal number of odd and even numbers.
The problem is to arrange the numbers in such a way that all the even numbers 
get the even index and odd numbers get the odd index.
Required auxiliary space is O(1).

Examples :

Input : arr[] = {3, 6, 12, 1, 5, 8}
Output : 6 3 12 1 8 5 

Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
Output : 10 9 18 7 20 19 4 13 14 21 

"""

class Solution():
  def arrange(self, nums):
    evenidx, oddidx = 0, 1
    while True:
      while evenidx < len(nums) and not nums[evenidx] % 2:
        evenidx += 2
      while oddidx < len(nums) and nums[oddidx] % 2:
        oddidx += 2
      if evenidx < len(nums) and oddidx < len(nums):
        nums[evenidx], nums[oddidx] = nums[oddidx], nums[evenidx]
      else:
        break

if __name__ == "__main__":
    # nums = [3, 6, 12, 1, 5, 8]
    nums = [10, 9, 7, 18, 13, 19, 4, 20, 21, 14]
    sol = Solution()
    sol.arrange(nums)
    print(nums)
      
      
