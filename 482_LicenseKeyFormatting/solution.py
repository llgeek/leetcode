class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')[::-1].upper()
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]

s = Solution()
S = "2-5g-3-J"
K = 2
print(s.licenseKeyFormatting(S, K))
