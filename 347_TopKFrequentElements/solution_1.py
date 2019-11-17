class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left, right = 0, 0
        cnt = {}
        ans = []
        for c in p:
          cnt[c] = cnt.get(c, 0) + 1
        need = len(p)
        rest = cnt.copy()
        while right < len(s):
          if s[right] not in cnt:
            left = right + 1
            rest = cnt.copy()
            need = len(p)
          else:
            rest[s[right]] -= 1
            need -= 1
            while rest[s[right]] < 0 and left <= right:
              rest[s[left]] += 1
              need += 1
              left += 1
            if need == 0:
              ans.append(left)
          right += 1
        return ans