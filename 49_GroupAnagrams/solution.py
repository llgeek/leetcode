from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hashtokey(word):
            cnt = sorted(Counter(word).items(), key = lambda x: x[0])
            key = [str(pair[1])+pair[0] for pair in cnt]
            return ''.join(key)
        
        anagrams = dict()
        for word in strs:
            key = hashtokey(word)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return [anagrams[key] for key in anagrams.keys()]

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
