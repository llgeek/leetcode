

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend == - (1<<31) and divisor == -1) or divisor == 0:
            return (1<<31) - 1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -1 * dividend
        if dividend == divisor:
            return 1
        if dividend == -1*divisor:
            return -1
        flag = 1 if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 else -1
        res = 0
        while abs(dividend) >= abs(divisor):
            i = 0
            tmpdivisor = divisor
            while tmpdivisor < 1<<30 and abs(tmpdivisor<<1) < abs(dividend):
                tmpdivisor <<= 1
                i += 1
            dividend -= flag * tmpdivisor
            res += (1<<i)
        return res * flag

if __name__ == "__main__":
    dividend = 7
    divisor = -3
    sol = Solution()
    print(sol.divide(dividend, divisor))
            

