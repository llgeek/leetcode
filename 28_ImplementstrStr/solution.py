"""
KMP method

O(m+n) time complexity
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def computePrefix(needle):
            prefix = [0] * len(needle)
            i = 0
            for j in range(1,len(needle)):
                while i > 0 and  needle[i] != needle[j]:
                    i = prefix[i-1]
                if needle[i] == needle[j]:
                    i += 1
                prefix[j] = i
            return prefix

        if not needle:
            return 0
        if not haystack:
            return -1
        prefix = computePrefix(needle)
        i = 0
        for j in range(len(haystack)):
            while i > 0 and needle[i] != haystack[j]:
                i = prefix[i-1]
            if needle[i] == haystack[j]:
                i += 1
            if i == len(needle):
                return j - i + 1
        return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    # haystack = "aaaaa"
    # needle = "bba"
    # haystack = ''
    # needle = ''
    # haystack = "mississippi"
    haystack = "mississippi"
    # needle = "issipi"
    needle = "issipi"
    # needle = 'pi'
    sol = Solution()
    print(sol.strStr(haystack, needle))

