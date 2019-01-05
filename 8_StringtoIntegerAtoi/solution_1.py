

class Solution:
    def myAtoi(self, numstr):
        """
        :type str: str
        :rtype: int
        """
        numchar = set('1234567890')
        numval = dict(zip(numchar, map(int, numchar)))
        numstr = numstr.strip(' ')
        if not numstr or numstr[0] not in (numchar | {'+', '-'}):
            return 0
        idx = 0
        flag = 1
        if numstr[0] == '+':
            flag = 1
            idx += 1
        if numstr[0] == '-':
            flag = -1
            idx += 1
        val = 0
        INTMAX = (1<<31)-1
        INTMIN = - (1<<31)
        while idx < len(numstr) and numstr[idx] in numchar:
            if val > INTMAX//10 or (val == INTMAX//10 and (numval[numstr[idx]] > 7 if flag==1 else numval[numstr[idx]] > 8)): 
                return INTMAX if flag == 1 else INTMIN 
            val = val * 10 + numval[numstr[idx]]
            idx += 1
        return flag * val

    
if __name__ == "__main__":
    # numstr = "   -42 with words"
    # numstr = "words and 987"
    # numstr = "-91283472332"
    numstr = "-3924x8fc"
    sol = Solution()
    print(sol.myAtoi(numstr))


