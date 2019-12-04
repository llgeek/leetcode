"""
backtracker will get TLE

use DP!
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        def helper(s, sid, p, pid):
          if (sid, pid) in self.memo:
            return self.memo[(sid, pid)]
          if sid >= len(s):
            if pid >= len(p):
              res = True
            else:
              if pid + 1 < len(p) and p[pid+1] == '*':
                res = helper(s, sid, p, pid + 2)
              else:
                res = False
            self.memo[(sid, pid)] = res
          elif pid >= len(p):
            self.memo[(sid, pid)] = False
          else:
            if pid + 1 < len(p) and p[pid+1] == '*':
              self.memo[sid, pid] = helper(s, sid, p, pid+2)
              if s[sid] == p[pid] or p[pid] == '.':
                self.memo[sid, pid] |= helper(s, sid+1, p, pid)
            else:
              if s[sid] == p[pid] or p[pid] == '.':
                self.memo[sid, pid] = helper(s, sid+1, p, pid+1)
              else:
                self.memo[sid, pid] = False
          return self.memo[sid, pid]
        return helper(s, 0, p, 0)
              
          
if __name__ == "__main__":
    # s = "aa"
    # p = "a"
    # s = "a"
    # p = "ab*"
    # s = "bbbba"
    # p = ".*a*a"
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"
    sol = Solution()
    print(sol.isMatch(s, p))