class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
          return "0"
        res = [0] * (len(num1) + len(num2))
        carry = 0
        if len(num1) > len(num2):
          num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
          carry = 0
          for j in range(len(num2)):
            product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
            carry, m = divmod(product, 10)
            m += res[i+j]
            if m > 9:
              carry += m // 10
              m %= 10
            res[i+j] = m
          if carry:
            res[i + len(num2)] += carry
        ret = ''.join(map(str, res[::-1])).lstrip('0')
        return ret if ret else '0'

if __name__ == "__main__":
    num1 = '99'
    num2 = '32'
    sol = Solution()
    print(sol.multiply(num1, num2))
