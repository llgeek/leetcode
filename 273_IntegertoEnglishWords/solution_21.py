class Solution:
    ONES = "One Two Three Four Five Six Seven Eight Nine".split(' ')
    TENS = "Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    OVERTENS = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    UNIT = " Thousand Million Billion".split(' ')
    
    def numberToWords(self, num: int) -> str:
        def convertToHundred(val):
            res = []
            if val >= 100:
                q, val = divmod(val, 100)
                res.append(self.ONES[q-1])
                res.append('Hundred')
            if val >= 20:
                q, val = divmod(val, 10)
                res.append(self.OVERTENS[q-2])
            if val >= 10:
                res.append(self.TENS[val-10])
                val = 0
            if val > 0:
                res.append(self.ONES[val-1])
            return res
                
        ret = []
        for i in range(4):
            if num:
                num, rem = divmod(num, 1000) 
                res= convertToHundred(rem)
                if res:
                    ret = res + [self.UNIT[i]] + ret
                
        return " ".join(ret).strip(' ') if ret else "Zero"
    

               