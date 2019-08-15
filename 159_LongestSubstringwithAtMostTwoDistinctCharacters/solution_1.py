class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, k) -> str:
        ans = 0, 0
        left = 0
        have = [0] * 128
        unique = 0
        for right, c in enumerate(s, 1):
            if have[ord(c)] == 0:
                unique += 1
            have[ord(c)] += 1
            while unique > k:
                have[ord(s[left])] -= 1
                if not have[ord(s[left])]:
                    unique -= 1
                left += 1
            if right - left > ans[1] - ans[0]:
                ans = left, right
        return s[ans[0]: ans[1]]


if __name__ == '__main__':
    s = "abcabbcdaabbcc"
    k = 3
    print(Solution().lengthOfLongestSubstringTwoDistinct(s, k))

            
        