"""
second trial

DFS

https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
"""


class Solution:
    def __init__(self):
        self.ans = []
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        def remove(checkstr, last_i, last_j, pair):
            cnt = 0
            for i in range(last_i, len(checkstr)):
                if checkstr[i] == pair[0]:
                    cnt += 1
                elif checkstr[i] == pair[1]:
                    cnt -= 1
                if cnt >= 0:
                    continue
                for j in range(last_j, i+1):
                    if checkstr[j] == pair[1] and (j == last_j or checkstr[j] != checkstr[j-1]):
                        remove(checkstr[:j] + checkstr[j+1:], i, j, pair)
                return
            checkstr = checkstr[::-1]
            if pair[0] == "(":
                remove(checkstr, 0, 0, ')(') 
            else:
                self.ans.append(checkstr)
        remove(s, 0, 0, "()")
        return self.ans
    
if __name__ == "__main__":
    # s = "()())()"
    # s =  "(a)())()"
    # s  = ")("
    # s = "(a)())()"
    # s = "(a)())()"
    s = "(()"
    sol = Solution()
    print(sol.removeInvalidParentheses(s))
        
        