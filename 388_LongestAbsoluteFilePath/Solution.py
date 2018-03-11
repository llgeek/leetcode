class Solution:

    def LengthLongestPath(self, input):
        """
        type input: str
        rtype: int
        """
        maxlen = 0
        level2depth = {0:0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            curdepth = len(line) - len(name)
            if '.' in line:
                maxlen = max(maxlen, level2depth[curdepth] + len(name))
            else:
                level2depth[curdepth+1] = level2depth[curdepth] + len(name) + 1
        return maxlen

s = Solution()
dir = "dir1\n\tdddddddddddddd\n\tdir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.LengthLongestPath(dir))