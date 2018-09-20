import time
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        maxlen = 1
        ret = s[0]
        mark = [[1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if maxlen < 2:
                    maxlen = 2
                    ret = s[i:i+2]
                mark[i][i+1] = 2
            
        for l in range(3, len(s)+1):
            for i in range(len(s)-l+1):
                j = i + l - 1
                if mark[i+1][j-1] == l-2 and s[i] == s[j]:
                    mark[i][j] = l 
                    if l > maxlen:
                        maxlen = l
                        ret = s[i:j+1]
                # else:
                #     mark[i][j] = max(mark[i+1][j], mark[i][j-1])
        return ret 
    

if __name__ == '__main__':
    s = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    # s = "cbbd"
    st = time.time()
    print(Solution().longestPalindrome(s))
    print('time: ', time.time()-st)

                
                
