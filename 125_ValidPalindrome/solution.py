import string
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin, end = 0, len(s)-1
        letters = set(string.ascii_lowercase) | set(string.ascii_uppercase)
        digits = set(string.digits)
        while begin < end:
            while begin < end and s[begin] not in (letters | digits):
                begin += 1
                continue
            while begin < end and s[end] not in (letters | digits):
                end -= 1
                continue
            if s[begin] == s[end] or (s[begin] in letters and s[end] in letters and abs(ord(s[begin]) - ord(s[end])) == abs(ord('A') - ord('a'))):
                continue
            else:
                return False
            begin += 1

            end -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "0P"
    print(sol.isPalindrome(s))