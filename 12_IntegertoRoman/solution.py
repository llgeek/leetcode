

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romval = ''
        while num:
            if num >= 1000:
                romval += 'M' * (num//1000)
                num %= 1000
            elif num >= 900:
                romval += 'CM'
                num -= 900
            elif num >= 500:
                romval += 'D'
                num -= 500
            elif num >= 400:
                romval += 'CD'
                num -= 400
            elif num >= 100:
                romval += 'C' * (num//100)
                num %= 100
            elif num >= 90:
                romval += 'XC'
                num -= 90
            elif num >= 50:
                romval += 'L'
                num -= 50
            elif num >= 40:
                romval += 'XL'
                num -= 40
            elif num >= 10:
                romval += 'X' * (num//10)
                num %= 10
            elif num == 9:
                romval += 'IX'
                num -= 9
            elif num >= 5:
                romval += 'V'
                num -= 5
            elif num == 4:
                romval += 'IV'
                num -= 4
            else:
                romval += 'I' * num
                num = 0
        return romval
    

if __name__ == "__main__":
    num = 3999
    sol = Solution()
    print(sol.intToRoman(num))
