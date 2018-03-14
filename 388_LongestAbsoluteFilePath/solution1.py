class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        inputlist = input.split('\n')
        maxlen = 0
        stack = []
        prelevel = -1
        for dirorfile in inputlist:
            curlevel = len(dirorfile) - len(dirorfile.lstrip('\t'))
            dirorfile = dirorfile.lstrip('\t')
            if curlevel <= prelevel:
                prelen, prelvl = stack[-1]
                while prelvl >= curlevel and stack:
                    prelen, prelvl = stack.pop()
                if prelvl < curlevel:
                    stack.append((prelen, prelvl))
            if '.' in dirorfile:
                maxlen = max((stack[-1][0] if stack else 0) + len(dirorfile), maxlen)
                continue
            prelevel = curlevel
            stack.append((len(dirorfile) + (stack[-1][0] if stack else 0) + 1, curlevel))
        return maxlen

s = Solution()
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.lengthLongestPath(input))
            
