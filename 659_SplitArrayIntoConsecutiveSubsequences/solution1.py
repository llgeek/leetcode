from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        append_freq = dict()
        for val in nums:
            if cnt[val] == 0:
                continue
            elif append_freq.get(val, 0) > 0:
                append_freq[val] -= 1
                append_freq[val + 1] = append_freq.get(val + 1, 0) + 1
            elif cnt.get(val + 1, 0) > 0 and cnt.get(val + 2, 0) > 0:
                cnt[val+1] -= 1
                cnt[val+2] -= 1
                append_freq[val + 3] = append_freq.get(val + 3, 0) + 1
            else:
                return False
            cnt[val] -= 1
        return True