class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = 0
        res = -float('inf')
        cnt = {}
        diffnum = 0
        for right, c in enumerate(s):
            # if c in cnt:
            #     cnt[c] += 1
            # else:
            #     cnt[c] = 1
            #     diffnum += 1
            if cnt.get(c, 0) == 0:
                diffnum += 1
            cnt[c] = cnt.get(c, 0) + 1
            while diffnum > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    diffnum -= 1
                left += 1
            res = max(res, right-left+1)
        return max(res, 0)

if __name__ == "__main__":
    s = 'eceba'
    # s = ''
    k = 2
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct(s, k))
