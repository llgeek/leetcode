"""
second trial

backtrack and DFS based solution

"""
class Solution:
    def __init__(self):
        self.res = set()
        self.min_removed = float('inf')

    def calc_missmatch_num(self, s):
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1
        return left, right
    def isvalid(self, s):
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                left -= 1
            if left < 0:
                return False
        return left == 0

    def backtracker(self, string, idx, leftnum, rightnum, missleft, missright, expr):
        if idx == len(string):
            if missleft == 0 and missright == 0:
                self.res.add("".join(expr))
        else:
            if (string[idx] == '(' and missleft > 0) or (string[idx] == ')' and missright > 0):
                self.backtracker(string, idx+1, leftnum, rightnum, 
                                missleft - (string[idx] == '('), missright - (string[idx] == ')'), expr)
            expr.append(string[idx])
            if string[idx] not in '()':
                self.backtracker(string, idx+1, leftnum, rightnum, missleft, missright, expr)
            elif string[idx] == '(':
                self.backtracker(string, idx+1, leftnum+1, rightnum, missleft, missright, expr)
            elif string[idx] == ')' and leftnum > rightnum:
                self.backtracker(string, idx+1, leftnum, rightnum+1, missleft, missright, expr)
            expr.pop()


    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        if self.isvalid(s):
            return [s]
        missleft, missright = self.calc_missmatch_num(s)
        self.backtracker(s, 0, 0, 0, missleft, missright, [])
        return list(self.res)

