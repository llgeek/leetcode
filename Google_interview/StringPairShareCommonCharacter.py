"""
给一组字符串,找出任意两个字符串有没有重复的字符,如果没有得到分数是两个字符串长度相乘,如果有得到0分, 求最大的分数
"""

class Solution(object):
    def rollinghash(self, s):
        encres = 0
        for c in s:
            encres |= 1 << (ord(c) - ord('a'))
        return encres
    
    def compareTwoStrs(self, s1, s2):
        encres1 = self.rollinghash(s1)
        encres2 = self.rollinghash(s2)
        return not encres1 & encres2

s1 = 'abac'
s2 = 'ddef'
print(Solution().compareTwoStrs(s1, s2))