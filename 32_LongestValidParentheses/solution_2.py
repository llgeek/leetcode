"""

traverse from left to right, and reverse the traversal
condition is: left >= right
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def removeleast(s, leftchar='(', rightchr=')'):
            maxres = 0
            left, right = 0, 0
            for i in range(len(s)):
                if s[i] == leftchar:
                    left += 1
                elif s[i] == rightchr:
                    right += 1
                if left == right:
                    maxres = max(maxres, right * 2)
                elif left < right:
                    left, right = 0, 0
            return maxres
        return max(removeleast(s), removeleast(s[::-1], ')', '('))

if __name__ == "__main__":
    sol = Solution()
    s = "()(()"
    print(sol.longestValidParentheses(s))
