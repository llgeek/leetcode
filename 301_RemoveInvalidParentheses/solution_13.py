"""
second trial

backtrack and DFS based solution

revised version, easier to follow
"""


class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        def isvalid(s):
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                if left < 0:
                    return False
            return left == 0
        
        def calc_missmatch_num(s):
            left, right = 0, 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right


        def backtracker(s, idx, missleft, missright, pair, path, res):
            if idx == len(s):
                if missleft == 0 and missright == 0 and pair == 0:
                    res.add("".join(path))
            else:
                if s[idx] == '(':
                    if missleft > 0:
                        backtracker(s, idx+1, missleft-1, missright, pair, path, res)
                    backtracker(s, idx+1, missleft, missright, pair+1, path+[s[idx]], res)
                elif s[idx] == ')':
                    if missright > 0:
                        backtracker(s, idx+1, missleft, missright-1, pair, path, res)
                    if pair > 0:
                        backtracker(s, idx+1, missleft, missright, pair-1, path+[s[idx]], res)
                else:
                    backtracker(s, idx+1, missleft, missright, pair, path+[s[idx]], res)

        if isvalid(s):
            return [s]
        
        missleft, missright = calc_missmatch_num(s)
        res = set()
        backtracker(s, 0, missleft, missright, 0, [], res)
        return list(res)
