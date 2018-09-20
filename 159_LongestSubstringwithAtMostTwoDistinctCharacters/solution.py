class Solution():
    def lengthOfLongestSubstringTwoDistinct(self, s, k):
        """
        Arguments:
            s {str} -- [input string]
            k {int} -- [substring at most k distinct characters, here k = 2]

            generalize the problem into k distinct characters
        
        Returns:
            [str] -- [substring with two distinct characters]
        """

        if len(s) < 3: return s
        start, end = 0, 0
        mark = {}
        maxlen = 1
        sid = 0
        while end < len(s):
            c = s[end]
            if c in mark:
                mark[c] += 1
            else:
                if len(mark) == k:
                    while len(mark) == k:
                        mark[s[start]] -= 1
                        if mark[s[start]] == 0:
                            mark.pop(s[start])
                        start += 1
                mark[c] = 1
            if end - start + 1 > maxlen:
                maxlen = end - start + 1
                sid = start
            end += 1
        return s[sid: sid+maxlen]

if __name__ == '__main__':
    s = "abcabbcdaabbcc"
    k = 3
    print(Solution().lengthOfLongestSubstringTwoDistinct(s, k))


