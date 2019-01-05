class Solution:
    def noPairsAllowed(self, word):
        prechr = '#'
        res = 0
        for c in word:
            if c == prechr:
                res += 1
                prechr = '#'
            else:
                prechr = c 
        return res
            

def processTests(inputfile):
    res = []
    sol = Solution()
    with open(inputfile, 'r') as rf:
        n = int(next(rf))
        for i in range(n):
            word = next(rf)
            res.append(sol.noPairsAllowed(word))
    return res


if __name__ == '__main__':
    infile = 'input.txt'
    print(processTests(infile))