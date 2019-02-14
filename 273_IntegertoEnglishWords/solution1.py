
class Solution:
    BELOW_TWENTIES = " One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve"\
                    " Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    TENS = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
    UNIT = "Thousand Million Billion".split()

    def numberToWords(self, num: 'int') -> 'str':
        def convertToHundred(num):
            ret = []
            if num >= 100:
                ret.extend([self.BELOW_TWENTIES[num//100], 'Hundred'])
                num %= 100
            if num >= 20:
                ret.append(self.TENS[num//10-2])
                num %= 10
            if num > 0:
                ret.append(self.BELOW_TWENTIES[num])
            return ret
        res = convertToHundred(num % 1000)
        i = 0
        num //= 1000
        while num:
            num, rem = divmod(num, 1000)
            if rem:
                res = convertToHundred(rem) + [self.UNIT[i]] + res
            i += 1
        res = " ".join(res).strip()
        return res if res else 'Zero'

if __name__ == "__main__":
    num = 50868
    sol = Solution()
    print(sol.numberToWords(num)) 

        
        

