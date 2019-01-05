class Solution:
    def myAtoi(self, _str):
        """
        :type _str: _str
        :rtype: int
        """
        _str = _str.strip()
        if not _str:
            return 0
        smapv = dict(zip(map(lambda x: str(x), range(10)), range(10)))
        num = 0
        sign = 1
        idx = 0
        # ifoverflow = False
        if _str[0] == '+':
            sign = 1
            idx += 1
        if _str[0] == '-':
            sign = -1
            idx += 1
        while idx < len(_str):
            if _str[idx] not in smapv:
                break
            num = num * 10 + smapv[_str[idx]]
            # if num % 10 != smapv[_str[idx]]:
            #     ifoverflow = True 
            #     break
            idx += 1
        # if ifoverflow:
        #     return 2 ** 31 - 1 if sign == 1 else - 2 ** 31
        num = num * sign
        return min(num, 2 ** 31 - 1) if num > 2 ** 31 - 1 else max(num, - 2 ** 31)

if __name__ == "__main__":
    # _str = "-91283472332"
    _str = "4193 with words"
    sol = Solution()
    print(sol.myAtoi(_str))
        
