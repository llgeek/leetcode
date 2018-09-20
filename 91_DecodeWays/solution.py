class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        memo = [0 for _ in range(len(s)+1)]
        memo[-1] = 1
        memo[-2] = 1 if s[-1] != '0' else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0' and s[i+1] == '0':
                return 0
            if s[i] == '0':
                continue
            if int(s[i:i+2]) <= 26:
                memo[i] = memo[i+1] + memo[i+2]
            else:
                memo[i] = memo[i+1]
        return memo[0]
   
                
    
if __name__ == '__main__':
    s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    # s = '1001'
    print(Solution().numDecodings(s))
