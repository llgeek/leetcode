class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or any((num1=='0', num2=='0')):
            return '0'
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        if num1 == '1':
            return num2
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num2)):
            carry = 0
            for j in range(len(num1)):
                tmp = carry + ((ord(num2[i]) - ord('0')) * (ord(num1[j]) - ord('0')))
                carry, tmp = divmod(tmp, 10)
                res[i+j] += tmp
                if res[i+j] > 9:
                    res[i+j] %= 10
                    carry += 1

            if carry:
                res[i + len(num1)] += carry
        res = ''.join(map(str, res[::-1])).lstrip('0')
        return res if res else '0'

if __name__ == "__main__":
    sol = Solution()
    num1 = "123"
    num2 = "456"
    print(sol.multiply(num1, num2))
