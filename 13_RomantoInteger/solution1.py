class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        chr2val = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        for i in range(len(s)):
            if prev < chr2val[s[i]]:
                val -= 2*prev
            val += chr2val[s[i]]
            prev = chr2val[s[i]]
        return val


if __name__ == "__main__":
    # s = 'LVIII'
    s = 'MMMCMXCIX'
    sol = Solution()
    print(sol.romanToInt(s))
