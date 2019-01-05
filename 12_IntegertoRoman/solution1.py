"""
pre-compute all possible values to reduce processing time
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romval = ''
        thousand = ['', 'M', 'MM', 'MMM']
        hundred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        romval += thousand[num//1000]
        num %= 1000
        romval += hundred[num//100]
        num %= 100
        romval += ten[num//10]
        num %= 10
        romval += one[num]
        return romval


if __name__ == "__main__":
    num = 3999
    sol = Solution()
    print(sol.intToRoman(num))
