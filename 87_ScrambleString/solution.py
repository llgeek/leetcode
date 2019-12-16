"""
dp
"""
from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[s1, s2]
            if s1 == s2:
                memo[s1, s2] = True
                return True
            if len(s1) != len(s2):
                memo[s1, s2] = False
                return False
            cnt1 = Counter(s1)
            cnt2 = Counter(s2)
            if len(cnt1) != len(cnt2):
                memo[s1, s2] = False
                return False
            for key in cnt1.keys():
                if key not in cnt2 or cnt1[key] != cnt2[key]:
                    memo[s1, s2] = False
                    return False
            for i in range(1, len(s1)):
                if helper(s1[0:i], s2[0:i]) and helper(s1[i:], s2[i:]):
                    memo[s1, s2] = True
                    return True
                if helper(s1[0:i], s2[len(s2)-i:]) and helper(s1[i:], s2[:len(s2)-i]):
                    memo[s1, s2] = True
                    return True
            memo[s1, s2] = False
            return False      

        