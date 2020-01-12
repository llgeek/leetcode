class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and stack[-1][1] < nums[i]:
                pos, val = stack[-1]
                res[pos] = nums[i]
                stack.pop()
            stack.append((i, nums[i]))
        for i in range(len(nums)):
            while stack and stack[-1][1] < nums[i]:
                pos, val = stack[-1]
                if res[pos] == -1:
                    res[pos] = nums[i]
                stack.pop()
            stack.append((i, nums[i]))
        return res

