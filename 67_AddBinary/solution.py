class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        idx = 0
        while idx < len(a) or idx < len(b):
            vala = int(a[::-1][idx]) if idx < len(a) else 0
            valb = int(b[::-1][idx]) if idx < len(b) else 0
            carry, val = divmod(vala + valb + carry, 2)
            result.append(str(val))
            idx += 1
        if carry:
            result.append(str(carry))
        return ''.join(result)[::-1]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a,b))