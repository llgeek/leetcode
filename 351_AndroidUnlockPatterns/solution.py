class Solution:
    def numberOfPatterns(self, m, n):
        """
        m: int, lower bound
        n: int, upper bound
        rtype int: number of unlock patterns
        """
        def helper(m, n, next, length, num):
            if length > n:
                return num
            if length >= m:
                num += 1
            isvisited[next] = True
            length += 1
            for neb in range(1, 10):
                jump = jumper[next][neb]
                if not isvisited[neb] and (jump == 0 or isvisited[jump]):
                    num = helper(m, n, neb, length, num)
            isvisited[next] = False
            return num
            
        isvisited = [False] * 10
        # jumper = [
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0]
        # ]
        jumper = [[0 for _ in range(11)] for _ in range(11)]
        jumper[1][3] = jumper[3][1] = 2
        jumper[4][6] = jumper[6][4] = 5
        jumper[7][9] = jumper[9][7] = 8
        jumper[1][7] = jumper[7][1] = 4
        jumper[2][8] = jumper[8][2] = 5
        jumper[3][9] = jumper[9][3] = 6
        jumper[1][9] = jumper[9][1] = jumper[3][7] = jumper[7][3] = 5
        res = 0
        res += helper(m, n, 1, 1, 0) * 4
        res += helper(m, n, 2, 1, 0) * 4
        res += helper(m, n, 5, 1, 0)
        return res


print(Solution().numberOfPatterns(5, 7))
