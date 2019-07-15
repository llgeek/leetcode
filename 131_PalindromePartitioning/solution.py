from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtracker(ret, s, path, startidx):
            if startidx >= len(s):
                ret.append(path[:])
            else:
                for i in range(startidx, len(s)):
                    if (startidx, i) not in self.memo:
                        self.memo[(startidx, i)] = validpalindrome(s[startidx:i+1])
                    if self.memo[(startidx, i)]:
                        path.append(s[startidx:i+1])
                        backtracker(ret, s, path, i+1)
                        path.pop() 

        def validpalindrome(substr):
            i, j = 0, len(substr)-1
            while i < j:
                if substr[i] != substr[j]:
                    return False
                i += 1
                j -= 1
            return True

        self.memo = {}
        ret = []
        backtracker(ret, s, [], 0)
        return ret

if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    print(sol.partition(s))