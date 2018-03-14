class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        numstr = ''
        for c in s:
            if '0' <= c <= '9':
                numstr += c 
            elif c == '[':
                stack.append(['', int(numstr)])
                numstr = ''
            elif c == ']':
                tmpstr, times = stack.pop()
                stack[-1][0] +=  times * tmpstr
            else:
                stack[-1][0] += c
        return stack[0][0]


sol = Solution()
s = "2[abc]3[cd]ef"
print(sol.decodeString(s))
                
            
                
