class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        res = (-1, (1<<31)-1 )
        left, right = 0, 0
        cnt = dict(Counter(t))
        chrnum = len(cnt)
        while right < len(s):
            if s[right] not in cnt:
                continue
            cnt[s[right]] -= 1
            if cnt[s[right]] == 0:
                chrnum -= 1
            if chrnum == 0 and right - left + 1 < res[1]:
                res = (left, right-left+1)
            while cnt[s[right]] < 0:
                if cnt[s[left]] == 0:
                    chrnum += 1 
                cnt[s[left]] += 1
                left += 1
            right += 1
        return s[res[0]:res[0]+res[1]] if res[0] != -1 else ""
            
