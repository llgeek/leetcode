"""
第二轮:自我介绍,题是面经里的,给定两个单词,问第二个单词能否通过交换第一个单词中两个字母得到 Follow up:能否通过交换至多n次得到
ANS : https://www.careercup.com/question?id=6464130037841920

Page 3

"""
from collections import defaultdict
class Solution:
    def metaWord(self, word1, word2):
        """
        Only one swap solution
        """
        if word1 == word2 or len(word1)!= len(word2):
            return False
        diffnum = 0
        wd1, wd2 = '', ''
        for idx, ch in enumerate(word1):
            if ch != word2[idx]:
                diffnum += 1
                if diffnum > 2:
                    return False
                wd1 += ch
                wd2 += word2[idx]
        return diffnum == 2 and wd1 == wd2[::-1]


    def metaWordMultipleSwap(self, word1, word2):
        """
        Check if can swap at most n times to make word2 be word1
        n = len(word1)
        """
        def checkSwappable(s1, s2, startidx):
            for i in range(startidx, len(s1)):
                if s1[i] != s2[i]:
                    chins2idx = self.char2swapidx.get(s1[i], set())
                    if chins2idx:
                        for idx in chins2idx:
                            print(s2, i)
                            print(s1, idx)
                            if idx > i:# and s2[i] == s1[idx]:
                                chins2idx.discard(idx)
                                chins2idx.add(i)
                                self.char2swapidx[s2[i]].discard(i)
                                self.char2swapidx[s2[i]].add(idx)
                                if checkSwappable(s1, s2[:i] + s2[idx] + s2[i+1:idx]+s2[i]+s2[idx+1:], i+1):
                                    return True
                                chins2idx.add(idx)
                                chins2idx.discard(i)
                                self.char2swapidx[s2[i]].add(i)
                                self.char2swapidx[s2[i]].discard(idx)
                    else:
                        return False
            return s1==s2


        if word1 == word2 or len(word1) != len(word2):
            return False
        self.char2swapidx = defaultdict(lambda : set())
        for idx, ch in enumerate(word1):
            if ch != word2[idx]:
                self.char2swapidx[word2[idx]].add(idx)
        return checkSwappable(word1, word2, 0)




s = Solution()
word1, word2 = 'abc', 'bca'
#print(s.metaWord(word1, word2))
print(s.metaWordMultipleSwap(word1, word2))