class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {num: -1 for num in nums1}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                top = stack.pop()
                if top in res:
                    res[top] = num
            stack.append(num)
        return [res[key] for key in nums1]