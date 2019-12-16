class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        skip = {'.', '..', '/', ''}
        for dir in path.split('/'):
            if dir in skip:
                if dir == '..' and stack:
                    stack.pop(-1)
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    sol = Solution()
    # path  ="/."
    path = "/..."
    print(sol.simplifyPath(path))