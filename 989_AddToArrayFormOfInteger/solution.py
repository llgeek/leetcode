class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        res = []
        A = A[::-1]
        i = 0
        carry = 0
        while i < len(A) and K:
            K, rem = divmod(K, 10)
            tmpsum = A[i] + rem + carry
            carry, tmpsum = divmod(tmpsum, 10)
            res.append(tmpsum)
            i += 1
        while i < len(A):
            tmpsum = A[i] + carry
            carry, tmpsum = divmod(tmpsum, 10)
            res.append(tmpsum)
            i += 1
        while K:
            K, rem = divmod(K, 10)
            tmpsum = rem + carry
            carry, tmpsum = divmod(tmpsum, 10)
            res.append(tmpsum)
        if carry:
            res.append(carry)
        return res[::-1]
