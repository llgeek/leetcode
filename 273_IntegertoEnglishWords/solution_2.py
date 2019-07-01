class Solution:
    ONES = "One Two Three Four Five Six Seven Eight Nine".split(' ')
    TENS = "Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    OVERTENS = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    UNIT = " Thousand Million Billion".split(' ')
    
    def numberToWords(self, num: int) -> str:
        def convertToHundred(val):
            ret = []
            if val >= 100:
                ret += [self.ONES[val//100-1], "Hundred"]
                val %= 100
            if val >= 20:
                ret += [self.OVERTENS[val//10-2]]
                val %= 10
            if val >= 10:
                ret += [self.TENS[val-10]]
                val = 0
            if val > 0:
                ret += [self.ONES[val-1]]
            return ret
        res = []
        for i in range(4):
            if num:
                num, remain = divmod(num, 1000)
                ret = convertToHundred(remain)
                if ret:
                    res = ret + [self.UNIT[i]] + res
        return " ".join(res).strip(' ') if res else 'Zero'

if __name__ == "__main__":
    num = 12345
    sol = Solution()
    print(sol.numberToWords(num))
     
                