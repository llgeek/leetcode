class Solution:
    def countSubstrings(self, s: str) -> int:
        def extendPalindrome(s, left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1

        self.res = 0
        for i in range(len(s)):
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i+1)
        return self.res
    
