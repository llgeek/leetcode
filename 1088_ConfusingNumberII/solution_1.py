class Solution:
    def findAllConfNums(self, N):
        def valid(val):
            res, tmp = 0, val
            while tmp:
                d, m = divmod(tmp, 10)
                if m not in mapping: return False
                res = res * 10 + mapping[m]
                tmp = d
            return res != val

        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        queue = [1, 6, 8, 9]
        visited = set()
        res = 0
        while queue:
            val = queue.pop()
            if val > N or val < 1: continue
            if val not in visited and valid(val):
                res += 1
                visited.add(val)
            for k in mapping.keys():
                queue.append(val * 10 + k)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllConfNums(1000000000))
