class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        c = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            v1 = 1 if i >= 0 and a[i] == '1' else 0
            v2 = 1 if j >= 0 and b[j] == '1' else 0
            c, r = divmod(v1 + v2 + c, 2)
            res.append(r)
            i -= 1
            j -= 1
        if c == 1:
            res.append(c)
        return "".join(map(str, res))[::-1]