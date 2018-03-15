class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return '0'
        if not num1:
            return num2
        if not num2:
            return num1
        n1, n2 = len(num1), len(num2)
        result = [0] * (max(n1, n2) + 1)
        carry = 0
        idx = 0
        while idx < n1 or idx < n2:
            v1, v2 = 0, 0
            if idx < n1:
                v1 = int(num1[::-1][idx])
            if idx < n2:
                v2 = int(num2[::-1][idx])
            carry, result[idx] = divmod(v1 + v2 + carry, 10)
            idx += 1
        result[-1] += carry
        while result and result[-1] == 0:
            result.pop()
        return ''.join(map(str, result[::-1]) if result else '0')

num1 = '9'
num2 = '9'
print(Solution().addStrings(num1, num2))