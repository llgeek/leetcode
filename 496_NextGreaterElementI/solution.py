class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = {num: -1 for num in nums1}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                if stack[-1] in res:
                    res[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return [res[num] for num in nums1]
