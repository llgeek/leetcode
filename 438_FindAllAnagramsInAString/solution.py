from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        cnt = dict(Counter(p))
        res = []
        left, right = 0, 0
        curcnt = cnt.copy()
        for right in range(len(s)):
            if s[right] not in curcnt:
                left = right + 1
                curcnt = cnt.copy()
                continue
            curcnt[s[right]] -= 1
            while curcnt[s[right]] < 0:
                curcnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p) and not any(curcnt.values()):
                res.append(left)
        return res

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc" 
    sol = Solution()
    print(sol.findAnagrams(s, p))