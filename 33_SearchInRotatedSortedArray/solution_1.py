class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0

        # TODO: use binary search to find pivot to make the program truly O(logn)
        for i in range(1, len(nums)):
          if nums[i] < nums[i-1]:
            pivot = i
            break

        trueidx = lambda idx: (idx + pivot) % len(nums)

        left, right = 0, len(nums)-1
        while left <= right:
          mid = (left + right) // 2
          truemid = trueidx(mid)
          if nums[truemid] == target:
            return truemid
          elif nums[truemid] > target:
            right = mid - 1
          else:
            left = mid + 1
        return -1