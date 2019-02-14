"""
second trial
"""


class Solution:
    BELOW20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    OVER20 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    UNIT = ['Thousand', 'Million', 'Billion']
    def numberToWords(self, num: 'int') -> 'str':
        def convertToHundred(num):
            res = []
            if num >= 100:
                rem, num = divmod(num, 100)
                res.append(self.BELOW20[rem-1])
                res.append('Hundred')
            if 20 <= num < 100:
                rem, num = divmod(num, 10)
                res.append(self.OVER20[rem-2])
            if num > 0:
                res.append(self.BELOW20[num-1])
            return res

        res = convertToHundred(num%1000)
        num //= 1000
        i = 0
        while num:
            tmpres = convertToHundred(num % 1000)
            if tmpres:
                res = tmpres + [self.UNIT[i]] + res
            num //= 1000
            i += 1
        res = ' '.join(res)
        return res if res else 'Zero'

if __name__ == "__main__":
    num = 50868
    sol = Solution()
    print(sol.numberToWords(num)) 

