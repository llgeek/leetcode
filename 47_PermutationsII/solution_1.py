from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        self.ans = []
        def helper(cnt, path):
            if len(path) == len(nums):
                self.ans.append(path[:])
                return
            for num in cnt:
                if cnt[num] > 0:
                    cnt[num] -= 1
                    helper(cnt, path + [num])
                    cnt[num] += 1
        helper(cnt, [])
        return self.ans


