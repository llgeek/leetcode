"""
time complexity O(S) 
S: total characters in strs
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return res
        maxid = min(len(s) for s in strs)
        for i in range(maxid):
            c = strs[0][i]
            if all(s[i] == c for s in strs):
                res += c 
            else:
                return res
        return res

if __name__ == "__main__":
    # strs = ["flower","flow","flight"]
    strs = []
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
