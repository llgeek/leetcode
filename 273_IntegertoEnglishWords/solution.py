
class Solution:
    def numberToWords(self, num: 'int') -> 'str':
        def convertToHundred(num):
            ret = []
            if num >= 100:
                ret += [ones[num//100], 'Hundred']
                num %= 100
            if num >= 20:
                ret += [overtens[num//10 * 10]]
                num %= 10
            if 20 > num >= 10:
                ret += [tens[num]]
            if 10 > num > 0:
                ret += [ones[num]]
            return ret

        ones = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 
                5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        tens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        overtens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 
                70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        others = ['', 'Thousand', 'Million', 'Billion']

        res = []
        for i in range(4):
            if num:
                num, rem = divmod(num, 1000)
                ret = convertToHundred(rem)
                if ret:
                    res =  (ret + [others[i]] + res) if i else ret
        return ' '.join(res) if res else 'Zero'


if __name__ == "__main__":
    num = 1234567
    sol = Solution()
    print(sol.numberToWords(num))

