class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def possible(bound):
            acc, num = 0, 0
            for val in nums:
                acc += val
                if acc > bound:
                    num += 1
                    acc = val
            num += acc > 0
            return num <= m


        begin, end = max(nums), sum(nums)
        while begin < end:
            mid = (begin + end) // 2
            okay = possible(mid)
            if okay:
                end = mid
            else:
                begin = mid + 1
        return end