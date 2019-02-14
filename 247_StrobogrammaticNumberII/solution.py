
class Solution:
    def allStrobogramaticalNumber(self, n):
        def recursive(m, n):
            if m == 0:
                return ['']
            if m == 1:
                return ['0', '1', '8']
            tmp = recursive(m-2, n)
            res = []
            for t in tmp:
                if m != n:
                    res.append('0' + t + '0')
                res.append('1' + t + '1')
                res.append('8' + t + '8')
                res.append('6' + t + '9')
                res.append('9' + t + '6')
            return res

        return recursive(n, n)
    
if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.allStrobogramaticalNumber(n))
