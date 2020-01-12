class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append((c, 1))
            else:
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)
            while stack and stack[-1][1] >= k:
                stack[-1] = (stack[-1][0], stack[-1][1] - k)
                if stack[-1][1] == 0:
                    stack.pop()
        return "".join(list(map(lambda x: x[0] * x[1], stack)))