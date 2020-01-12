"""
backtracker

error
"""


class Solution:
    def backtracker(self, s, p, sid, pid):
        def endswithstar(p, pid):
            while pid < len(p):
                if pid+1 < len(p) and p[pid+1] == '*':
                    pid += 2
                else:
                    return False
            return True
        if sid == len(s):
            if pid == len(p):
                return True
            else:
                return endswithstar(p, pid)
        if pid >= len(p):
            return False
        if p[pid] == '.':
            if pid+1 < len(p) and p[pid+1] == '*':
                return self.backtracker(s, p, sid+1, pid) or self.backtracker(s, p, sid+1, pid+2)
            else:
                return self.backtracker(s, p, sid+1, pid+1)
        if s[sid] != p[pid]:
            if pid + 1 < len(p) and p[pid+1] == '*':
                return self.backtracker(s, p, sid, pid+2)
            else:
                return False
        else:
            if pid+1 < len(p) and p[pid+1] == '*':
                return self.backtracker(s, p, sid+1, pid) or self.backtracker(s, p, sid+1, pid+2)
            else:
                return self.backtracker(s, p, sid+1, pid+1)



    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        return self.backtracker(s, p, 0, 0)

if __name__ == "__main__":
    # s = 'amississippiab'
    # p = "mis*is*p*."
    s = "bbbba"
    p = ".*a*a"

    sol = Solution()
    print(sol.isMatch(s, p))
