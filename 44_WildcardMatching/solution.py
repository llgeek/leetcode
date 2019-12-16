class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        def helper(sid, pid):
            if (sid, pid) in self.memo:
                return self.memo[sid, pid]
            if pid == len(p):
                self.memo[sid, pid] = sid >= len(s)
                return sid >= len(s)
            if sid == len(s):
                for i in range(pid, len(p)):
                    if p[i] != '*':
                        self.memo[sid, pid] = False
                        return False
                self.memo[sid, pid] = False
                return True
            if p[pid] == s[sid] or p[pid] == '?':
                self.memo[sid, pid] = helper(sid+1, pid+1)
            elif p[pid] == '*':
                self.memo[sid, pid] = any((helper(sid, pid+1),
                                        helper(sid+1, pid)))
            else:
                self.memo[sid, pid] = False
            return self.memo[sid, pid]
        if not s:
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True
        if not p:
            return not s
        return helper(0, 0)


if __name__ == "__main__":
    sol = Solution()
    s = "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab"
    p = "*aabb***aa**a******aa*"
    print(sol.isMatch(s, p))