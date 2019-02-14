"""
second trial
"""


class Solution:
    def validPalindrome(self, s: 'str') -> 'bool':
        def isPalindrome(s, start, end):
            i, j = start, end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s)-1
        ifdelete = False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif not ifdelete:
                addi, decj = False, False
                ifdelete = True
                if s[i+1] == s[j]:
                    addi = isPalindrome(s, i+1, j)
                if s[i] == s[j-1]:
                    decj = isPalindrome(s, i, j-1)
                return addi or decj
            else:
                return False
        return True



