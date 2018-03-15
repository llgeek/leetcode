class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return 0
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        for i1, c1 in enumerate(num1[::-1]):
            for i2, c2 in enumerate(num2[::-1]):
                result[i1+i2] += int(c1) * int(c2)
                carry, result[i1+i2] = divmod(result[i1+i2], 10)
                result[i1+i2+1] += carry
        while result and result[-1] == 0:
            result.pop()
        return ''.join(map(str,result[::-1]) if result else '0')

num1 = '90'
num2 = '90'
print(Solution().multiply(num1, num2))
