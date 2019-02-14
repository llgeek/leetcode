"""
second trial

pure string operation
"""


class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        res = []
        i, j = 0, 0
        a, b = a[::-1], b[::-1]
        carry = 0
        while i < len(a) and j < len(b):
            tmpsum = int(a[i]) + int(b[j]) + carry
            carry, tmpsum = divmod(tmpsum, 2)
            res.append(str(tmpsum))
            i += 1
            j += 1
        if j < len(b):
            i, a = j, b
        while i < len(a):
            tmpsum = int(a[i]) + carry
            carry, tmpsum = divmod(tmpsum, 2)
            res.append(str(tmpsum))
            i += 1
        if carry:
            res.append(str(carry))
        return ''.join(res)[::-1]
