from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursiveHelper(s, p, sidx, pidx):
            if sidx == len(s):
                return pidx == len(p) or (pidx + 1 < len(p) and p[pidx+1] == '*' and recursiveHelper(s, p, sidx, pidx+2))
            if pidx >= len(p):
                return sidx == len(s)
            if p[pidx] == '.' or s[sidx] == p[pidx]:
                if pidx + 1 < len(p) and p[pidx+1] == '*':
                    return recursiveHelper(s, p, sidx+1, pidx) or recursiveHelper(s, p, sidx, pidx+2)
                else:
                    return recursiveHelper(s, p, sidx+1, pidx+1)
            else:
                if pidx + 1 < len(p) and p[pidx+1] == '*':
                    return recursiveHelper(s, p, sidx, pidx+2)
                else:
                    return False
        return recursiveHelper(s, p, 0, 0)
                    
if __name__ == "__main__":
    s = "bbbba"
    p = ".*a*a"
    sol = Solution()
    print(sol.isMatch(s, p))