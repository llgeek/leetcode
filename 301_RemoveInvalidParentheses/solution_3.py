from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()

        def invalidnum(s):
            left, right = 0, 0
            for c in s:
                if c == '(':
                    left += 1
                if c == ')':
                    if left:
                        left -= 1
                    else:
                        right += 1
            return left, right
        
        def backtracker(path, idx, lefthave, righthave, leftremain, rightremain):
            if righthave > lefthave:
                return
            if idx == len(s):
                if leftremain == rightremain == 0:
                    self.res.add(path)
                return
            if s[idx] not in '()':
                backtracker(path + s[idx], idx+1, lefthave, righthave, leftremain, rightremain)
            if s[idx] == '(':
                if leftremain > 0:
                    backtracker(path, idx+1, lefthave, righthave, leftremain - 1, rightremain)
                backtracker(path + s[idx], idx+1, lefthave+1, righthave, leftremain, rightremain)
            if s[idx] == ')':
                if rightremain > 0:
                    backtracker(path, idx+1, lefthave, righthave, leftremain, rightremain - 1)
                if lefthave > righthave:
                    backtracker(path + s[idx], idx+1, lefthave, righthave+1, leftremain, rightremain)
        
        leftremain, rightremain = invalidnum(s)
        backtracker('', 0, 0, 0, leftremain, rightremain)
        return list(self.res)

if __name__ == "__main__":
    sol = Solution()
    s = "(a)())()"
    print(sol.removeInvalidParentheses(s))