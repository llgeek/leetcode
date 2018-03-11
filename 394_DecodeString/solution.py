class Solution:
    def decodeString(self, s):
        """
        type s: str
        rtype: str
        """
        stack = []
        stack.append(['', 1])
        val = ''
        for c in s:
            if c.isdigit():
                val += c
            elif c == '[':
                stack.append(['', int(val)])
                val = ''
            elif c == ']':
                tmpstr, times = stack.pop()
                stack[-1][0] += times * tmpstr
            else:
                stack[-1][0] += c
        return stack[0][0]

sol = Solution()
s = "2[abc]3[cd]ef"
print(sol.decodeString(s))