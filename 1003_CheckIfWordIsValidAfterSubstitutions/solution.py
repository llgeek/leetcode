class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        cnt = {'a':0, 'b':0, 'c':0}
        for c in S:
            cnt[c] += 1
            print(cnt)
            if not (cnt['a'] >= cnt['b'] & cnt['b'] >= cnt['c']):
                return False
            return cnt['a'] == cnt['b'] == cnt['c']
        
if __name__ == "__main__":
    S = "aabcbc"
    sol = Solution()
    print(sol.isValid(S))