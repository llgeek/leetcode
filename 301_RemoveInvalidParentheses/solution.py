
from collections import deque
class Solution():
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]

        BFS version
        """
        
        path = deque()
        visited = set()
        path.append(s)
        visited.add(s)
        level = False
        result = []
        while path:
            node = path.pop()
            if self.isvalidParenthesis(node):
                result.append(node)
                level = True
            if level:
                continue
            for i in range(len(node)):
                if node[i] != ')' and node[i] != '(':
                    continue
                ss = node[0:i] + node[i+1:]
                if ss not in visited:
                    path.appendleft(ss)
                    visited.add(ss)

        return result
    
    def isvalidParenthesis(self, s):
        num = 0
        for c in s:
            if c == ')':
                num -= 1
            if c == '(':
                num += 1
            if num < 0:
                return False
        return True if num == 0 else False      


if __name__ == '__main__':
    sol = Solution()
    s = "(a)())()"
    print(sol.removeInvalidParentheses(s))

         

