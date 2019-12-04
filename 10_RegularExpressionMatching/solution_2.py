
class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        def recursive(s, p, sid, pid):
            if sid == len(s):
                return pid == len(p) or (pid + 1 < len(p) and p[pid+1] == '*' and recursive(s, p, sid, pid+2))
            if pid >= len(p):
                return sid == len(s)
            if pid + 1 < len(p) and p[pid+1] == '*':
                if p[pid] != '.' and s[sid] != p[pid]:
                    return recursive(s, p, sid, pid+2)
                else:
                    return recursive(s, p, sid, pid+2) or recursive(s, p, sid+1, pid+2) or recursive(s, p, sid+1, pid)
            else:
                if p[pid] != '.' and s[sid] != p[pid]:
                    return False
                else:
                    return recursive(s, p, sid+1, pid+1)

        return recursive(s, p, 0, 0)


if __name__ == "__main__":
    # s = 'amississippiab'
    # p = "mis*is*p*."
    s = "bbbba"
    p = ".*a*a"
    # s = 'a'
    # p = 'aa*'
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"

    sol = Solution()
    print(sol.isMatch(s, p))
