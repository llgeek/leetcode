class Solution:
    def myAtoi(self, str: str) -> int:
        def valid(res, flag):
          if flag == 1 and res >= 1<<31:
            return (1<<31) - 1
          elif flag == -1 and res > 1<<31:
            return - 1<<31
          else:
            return flag * res
        res = 0
        flag = 1
        i = 0
        for i in range(len(str)):
          if str[i] != ' ': break
        if i == len(str): return res
        if str[i] == '-':
          flag = -1
          i += 1
        elif str[i] == '+':
          flag = 1
          i += 1
        for i in range(i, len(str)):
          if str[i] not in '0123456789':
            return valid(res, flag)
          nextres = res * 10 + (ord(str[i]) - ord('0'))
          if nextres // 10 != res:
            return (1<<31) -1 if flag == 1 else - 1<<31
          res = nextres
        return valid(res, flag)
        
if __name__ == "__main__":
    sol = Solution()
    str = "   -42"
    print(sol.myAtoi(str))