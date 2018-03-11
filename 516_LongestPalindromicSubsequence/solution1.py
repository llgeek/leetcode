"""
DP implementation

idea:
PS[i, j] = PS[i+1, j-1], if s[i] == s[j]
         = max(PS[i, j-1], PS[i+1, j]) if s[i] != s[j]
"""


class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Get LTE in leetcode, modify the solutin reducing space complexity from O(n^2) to O(n)
        # if not s:
        #     return 0
        # lps = [[1 for _ in range(len(s))] for __ in range(len(s))]
        # for j in range(len(s)):
        #     for i in range(j-1, -1, -1):
        #         if s[i] == s[j]:
        #             lps[i][j] = 2 + lps[i+1][j-1] if i+1 <= j-1 else 2
        #         else:
        #             lps[i][j] = max(lps[i+1][j], lps[i][j-1])
        # #return max(map(max, lps))
        # return lps[0][len(s)-1]

        n = len(s)
        if s == s[::-1]:
            return n
        lps = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            tmplps = lps[:]
            # tmplps stores current lps from i to n-1
            # lps stores the previous substring lps from i+1 to n-1
            # substring [i, n-1] only depends on substring [i+1, n-1] ([i, n-2] can be calculated in tmplps)
            tmplps[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    tmplps[j] = 2 + lps[j-1]
                else:
                    tmplps[j] = max(lps[j], tmplps[j-1])
            lps = tmplps[:]
        return lps[n-1]





s = Solution()
ss = '"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"'
print(s.longestPalindromeSubseq(ss))