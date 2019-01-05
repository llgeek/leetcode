"""
second trial

cannot initialize is_palind as [[False] * len(s)] * len(s)

time limit exceeded in leetcode

need to optimize

O(nlogn) time complexity, O(n^2) space complexity

"""

# import numpy as np
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        idx = -1
        # is_palind = np.array([[False] * len(s)] * len(s))
        is_palind = []
        for _ in range(len(s)):
            is_palind.append([False] * len(s))

        for l in range(len(s)):
            isset = False
            for i in range(len(s)):
                j = i + l 
                if j > len(s) - 1: continue
                if l == 0: is_palind[i][j] = True 
                elif l == 1: is_palind[i][j] = (s[i] == s[j])
                else:
                    is_palind[i][j] = (is_palind[i+1][j-1] and s[i]==s[j])
                if is_palind[i][j] and not isset:
                    maxlen = l + 1
                    idx = i
                    isset = True
        return s[idx:idx+maxlen]


if __name__ == "__main__":
    # s = "babad"
    # s = "cbbd"
    s = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    sol = Solution()
    print(sol.longestPalindrome(s))
