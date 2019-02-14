"""
second trial

backtracker

TLE
"""


class Solution:
    def backtracker(self, s, idx):
        if idx == len(s):
            return 1
        if s[idx] == '0':
            return 0
        if idx + 1 < len(s) and 10 <= int(s[idx:idx+2]) <= 26:
            return self.backtracker(s, idx+1) + self.backtracker(s, idx+2)
        else:
            return self.backtracker(s, idx+1)
    def numDecodings(self, s: 'str') -> 'int':
        if not s:
            return 0
        return self.backtracker(s, 0)

if __name__ == "__main__":
    s = "1787897759966261825913315262377298132516969578441236833255596967132573482281598412163216914566534565"
    sol = Solution()
    print(sol.numDecodings(s))
