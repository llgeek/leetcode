"""
给一个字符串，找到最长的repeating substring. 
一个repeating string是通过repeat一个substring组成的，比如"xxx" 是"x" repeat 3 次, 
"abcabc"是"abc" repeat 两次，都属于repeating string.
例如"xxabcabcyyy"应该返回"abcabc", 另外两个repeating substring "xx"和"yyy"都没它长。

"""

class Solution():
  def maxRepeatedSubstring(self, s):
    