class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        assert divisor != 0, "divisor cannot be 0!"
        if dividend == -1<< 31 and divisor == -1:
            return (1<<31) - 1
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        if divisor == dividend:
            return 1
        if dividend == 0:
            return 0
        flag = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            flag = -1
        res = 0
        while abs(dividend) > abs(divisor):
            tmp = divisor
            i = 0
            while abs(dividend) >= abs(tmp):
                tmp = tmp << 1
                i += 1
            res += 1<<(i-1)
            dividend -= flag * (tmp >> 1)
        return res * flag

if __name__ == "__main__":
    sol = Solution()
    dividend = 7
    divisor = -3
    print(sol.divide(dividend, divisor))
            

        