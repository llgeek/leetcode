"""
second trial

BFS 

time complexity: n*2^n
"""

from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        def isValid(s):
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                if left < 0:
                    return False
            return left == 0
            
        if isValid(s):
            return [s]
        res = set()
        visited = set()
        resdepth = None
        queue = deque()
        queue.append((s, 0))
        visited.add(s)
        while queue:
            ss, removelen = queue.popleft()
            if resdepth is not None and removelen > resdepth:
                continue
            if isValid(ss):
                resdepth = removelen if resdepth is None else resdepth
                if removelen == resdepth:
                    res.add(ss)
            else:
                for i in range(len(ss)):
                    if ss[i] in '()':
                        nextss = ss[0:i] + ss[i+1:]
                        if nextss not in visited:
                            visited.add(nextss)
                            queue.append((nextss, removelen+1))
        return list(res)

if __name__ == "__main__":
    s = "()((((((()l("
    sol = Solution()
    print(sol.removeInvalidParentheses(s))
