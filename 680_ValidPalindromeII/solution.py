class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin, end = 0, len(s)-1
        while begin < end:
            if s[begin] == s[end]:
                begin += 1
                end -= 1
            else:
                if s[begin:end] == s[begin:end][::-1] or s[begin+1:end+1] == s[begin+1:end+1][::-1]:
                    return True
                else:
                    return False
        return True
        

if __name__ == '__main__':
    s = 'abca'
    sol = Solution()
    print(sol.validPalindrome(s))