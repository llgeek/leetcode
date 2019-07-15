class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        assert divisor != 0, 'divisor cannot be 0'
        
        MAXPOS = (1<<31)-1
        MAXNEG = -1<<31
        
        if dividend == 0:
            return 0
        if dividend == MAXNEG:
            if divisor == -1:
                return MAXPOS
            elif divisor == 1:
                return MAXNEG
            else:
                return self.divide(dividend+1, divisor) if divisor & 1 else self.divide(dividend>>1, divisor>>1)
        if divisor == MAXNEG:
            return 0
            
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            m = 1
            while tmp << 1 <= dividend:
                m <<= 1
                tmp <<= 1
            dividend -= tmp
            res += m
        return res * sign
