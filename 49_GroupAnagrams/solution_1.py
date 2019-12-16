from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def unordered_map(string):
            res = ''
            cnt = Counter(string)
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c in cnt:
                    res += '{}{}'.format(c, cnt[c])
            return res
        group = dict()
        for string in strs:
            key = unordered_map(string)
            group[key] = group.get(key, []) + [string]
        return [val for val in group.values()]

