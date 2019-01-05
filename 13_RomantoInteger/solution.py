class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        chr2val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        idx = 0
        while idx < len(s):
            if idx + 1 < len(s) and chr2val[s[idx]] < chr2val[s[idx+1]]:
                val += (chr2val[s[idx+1]] - chr2val[s[idx]])
                idx += 2
            else:
                val += chr2val[s[idx]]
                idx += 1
        return val


if __name__ == "__main__":
    s = 'LVIII'
    sol = Solution()
    print(sol.romanToInt(s))
