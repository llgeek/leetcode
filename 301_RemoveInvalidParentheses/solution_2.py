from typing import List
class Solution:
    def __init__(self):
        self.RES = set()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        def calc_minimum_remove(s):
            left, right = 0, 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left + right
        def backtrack(s, prev, left, right, idx, rmnum):
            while idx < len(s) and s[idx] not in '()':
                prev += s[idx]
                idx += 1
            if idx == len(s):
                if left == right and rmnum == 0:
                    self.RES.add(prev)
                return

            if left < right or rmnum < 0:
                return
            elif left > right:
                if s[idx] == '(':
                    backtrack(s, prev+'(', left+1, right, idx+1, rmnum)
                else:
                    backtrack(s, prev+')', left, right+1, idx+1, rmnum)
                backtrack(s, prev, left, right, idx+1, rmnum - 1)
            else:
                if s[idx] == '(':
                    backtrack(s, prev+'(', left+1, right, idx+1, rmnum)
                backtrack(s, prev, left, right, idx+1, rmnum - 1)    
        rmnum = calc_minimum_remove(s)       
        backtrack(s, '', 0, 0, 0, rmnum)
        return list(self.RES)

if __name__ == "__main__":
    # s = "()())()"
    # s =  "(a)())()"
    # s  = ")("
    # s = "(a)())()"
    s = "(a)())()"
    sol = Solution()
    print(sol.removeInvalidParentheses(s))
    
    """
    "(a)())()"
    Output
    ["()()()","(())()","(a)()()","(a())()"]
    Expected
    ["(a())()","(a)()()"]
    """